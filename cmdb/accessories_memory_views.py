# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Accessories_Memory 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import Accessories_MemoryForm
import cmdb_log

@login_required
def memory_get(request):
    if request.method == 'GET':
        objects_list = Accessories_Memory.objects.all()
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
        return render(request,'accessories_memory_list.html',context)

@login_required
@permission_required('cmdb.change_accessories_memory',raise_exception=True)
def memory_add(request):
    form = Accessories_MemoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.SN,data)
        return redirect('accessories_memory_get')
    return render(request, 'accessories_memory_form.html', {'form':form})

@login_required
@permission_required('cmdb.change_accessories_memory',raise_exception=True)
def memory_edit(request,pk):
    object = get_object_or_404(Accessories_Memory,pk=pk)
    object_data = object.__dict__.copy()
    form = Accessories_MemoryForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['SN'],message)
        return redirect('accessories_memory_get')
    return render(request,'accessories_memory_form.html', {'form':form})

@login_required
@permission_required('cmdb.change_accessories_memory',raise_exception=True)
def memory_delete(request,pk):
    object= get_object_or_404(Accessories_Memory,pk=pk)
    object_data = object.__dict__.copy()
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.SN,object_data)
        return redirect('accessories_memory_get')
    return render(request,'accessories_memory_confirm_delete.html', {'object':object})

@login_required
def memory_search(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        search_value = request.GET['search_value']
        if search_value:
            params = { search_key+'__startswith':search_value}
            objects_list = Accessories_Memory.objects.filter(**params).order_by(search_key)
        else:
            objects_list = Accessories_Memory.objects.all().order_by(search_key)
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
        return render(request,'accessories_memory_list.html',context)
