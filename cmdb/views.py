# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.admin.models import LogEntry
from cmdb.models import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
import cmdb_log
from form import LoginForm
def login(request):
    form = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                request.session.set_expiry(3600)
                auth.login(request, user)
                return redirect('/cmdb')
            else:
                result = '账号或密码错误'
                cmdb_log.log_login(username,result)
                form = LoginForm()
                context = {'form':form,'result':result}
                context.update(csrf(request))
                return render(request,'login.html',context)
    else:
        form = LoginForm()
        context = {'form':form}
        context.update(csrf(request))
        return render(request,'login.html',context)
@login_required
def index(request):
        context = {}
        return render(request,'index.html',context)
@login_required
def user(request):
        context = {}
        return render(request,'user.html',context)
    
@login_required
def logout(request):
        auth.logout(request)
        username = request.user.username
        cmdb_log.log_logoff(username)
        return redirect("/cmdb/login")
@login_required
def get_userinfo(request):
    context = {'username':request.user.last_name+request.user.first_name}
    return HttpResponse(json.dumps(context))
    
@login_required
def changepw(request):
    if request.method == 'POST':
        oldpwd = request.POST['oldpwd']
        newpwd = request.POST['newpwd']
        repwd = request.POST['repwd']
        if repwd != newpwd:
            context = {"result":"两次输入的密码不一致"}
            return render(request,'changepw.html',context)
        newpwd = request.POST['newpwd']
        if request.user.check_password(oldpwd):
            request.user.set_password(newpwd)
            request.user.save()
            context = {"result":"密码已修改"}
            return render(request,'changepw.html',context)
        else:
            context = {"result":"账号或密码不正确"}
            return render(request,'changepw.html',context)
    return render(request,'changepw.html') 
    
    
@login_required
def get_login_log(request):
    if request.method == 'GET':
        objects_list = Loginlog.objects.all().order_by('-id')
        num = objects_list.count()
        paginator = Paginator(objects_list,15)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context = {'objects':objects,'total':num}
        return render(request,'loginlog_list.html',context)
@login_required
def search_login_log(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        search_value = request.GET['search_value']
        if search_value:
            params = { search_key+'__startswith':search_value}
            objects_list = Loginlog.objects.filter(**params).order_by(search_key)
        else:
            objects_list = Loginlog.objects.all().order_by(search_key)
        num = objects_list.count()
        paginator = Paginator(objects_list,15)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context = {'objects':objects,'total':num,'search_key':search_key,'search_value':search_value}
        return render(request,'loginlog_list.html',context)

@login_required
def get_op_log(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        objects = LogEntry.objects.all().order_by('-id')
        num = LogEntry.objects.count()
        paginator = Paginator(objects,15)
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context = {'objects':objects,'total':num}
        return render(request,'oplog_list.html',context)


@login_required
def search_op_log(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        search_value = request.GET['search_value']
        if search_value: 
            if search_key == 'user':
                id = User.objects.get(username=search_value).id
                objects_list = LogEntry.objects.filter(user=id).order_by('-id')
            elif search_key == 'content_type':
                id = ContentType.objects.get(name=search_value).id
                objects_list = LogEntry.objects.filter(content_type=id).order_by('-id')
            else:
                params = { search_key+'__startswith':search_value}
                objects_list = LogEntry.objects.filter(**params).order_by(search_key)
               
        else:
            objects_list = LogEntry.objects.all().order_by(search_key)
        num = objects_list.count()
        paginator = Paginator(objects_list,15)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context = {'objects':objects,'total':num,'search_key':search_key,'search_value':search_value}
        return render(request,'oplog_list.html',context)

@login_required
def get_op_detail(request,pk):
    object = get_object_or_404(LogEntry,pk=pk)
    #return render(request,'oplog_detail.html', {'object':object})
    return HttpResponse(object.change_message)
