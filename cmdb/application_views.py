# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Application
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import ApplicationForm
import cmdb_log
from excellib import create_application_excel

@login_required
def application_get(request):
    if request.method == 'GET':
        objects = Application.objects.all()
        context = {'objects':objects}
        return render(request,'application_list.html',context)

@login_required
@permission_required('cmdb.change_application',raise_exception=True)
def application_add(request):
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.service,data)
        return redirect('application_get')
    return render(request, 'application_form.html', {'form':form})

@login_required
@permission_required('cmdb.change_application',raise_exception=True)
def application_edit(request,pk):
    object = get_object_or_404(Application,pk=pk)
    object_data = object.__dict__.copy()
    form = ApplicationForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['service'],message)
        return redirect('application_get')
    return render(request,'application_form.html', {'form':form})

@login_required
@permission_required('cmdb.change_application',raise_exception=True)
def application_delete(request,pk):
    object= get_object_or_404(Application,pk=pk)
    object_data = object.__dict__.copy()
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.service,object_data)
        return redirect('application_get')
    return render(request,'application_confirm_delete.html', {'object':object})


@login_required
def application_search(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        search_value = request.GET['search_value']
        if search_value:
            params = { search_key+'__contains':search_value}
            objects_list = Application.objects.filter(**params).order_by(search_key)
        else:
            objects_list = Application.objects.all().order_by(search_key)
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
        return render(request,'application_list.html',context)

@login_required
def application_detail(request,pk):
    object = get_object_or_404(Application,pk=pk)
    return render(request,'application_detail.html', {'object':object})

@login_required
def application_export(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        search_value = request.GET['search_value']
        if search_value:
            params = { search_key+'__contains':search_value}
            objects = Application.objects.filter(**params).order_by(search_key)
        else:
            objects = Application.objects.all().order_by(search_key)
        xls,fname = create_application_excel(objects)
        response = HttpResponse(mimetype="application/ms-excel")
        response['Content-Disposition'] = 'attachment;filename=%s.xls' % fname
        xls.save(response)
        return response
