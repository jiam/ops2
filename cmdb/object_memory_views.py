# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Memory,HostPhysical 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import MemoryForm
import cmdb_log

@login_required
def memory_get(request):
    if request.method == 'GET':
        objects = Memory.objects.all()
        context = {'objects':objects}
        return render(request,'object_memory_list.html',context)

@permission_required('cmdb.change_memory',raise_exception=True)
@login_required
def memory_add(request):
    form = MemoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Memory_Type,data)
        return redirect('object_memory_get')
    return render(request, 'object_memory_form.html', {'form':form})

@permission_required('cmdb.change_memory',raise_exception=True)
@login_required
def memory_edit(request,pk):
    object = get_object_or_404(Memory,pk=pk)
    object_data = object.__dict__.copy()
    form = MemoryForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Memory_Type'],message)
        return redirect('object_memory_get')
    return render(request,'object_memory_form.html', {'form':form})

@permission_required('cmdb.change_memory',raise_exception=True)
@login_required
def memory_delete(request,pk):
    object= get_object_or_404(Memory,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(memory=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Memory_Type,object_data)
        return redirect('object_memory_get')
    return render(request,'object_memory_confirm_delete.html', {'object':object})
