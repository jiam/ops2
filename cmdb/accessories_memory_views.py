# -*- coding: utf-8 -*-
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
        objects = Accessories_Memory.objects.all()
        context = {'objects':objects}
        return render(request,'accessories_memory_list.html',context)

@permission_required('cmdb.change_accessories_memory',raise_exception=True)
@login_required
def memory_add(request):
    form = Accessories_MemoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.SN,data)
        return redirect('accessories_memory_get')
    return render(request, 'accessories_memory_form.html', {'form':form})

@permission_required('cmdb.change_accessories_memory',raise_exception=True)
@login_required
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

@permission_required('cmdb.change_accessories_memory',raise_exception=True)
@login_required
def memory_delete(request,pk):
    object= get_object_or_404(Accessories_Memory,pk=pk)
    object_data = object.__dict__.copy()
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.SN,object_data)
        return redirect('accessories_memory_get')
    return render(request,'accessories_memory_confirm_delete.html', {'object':object})
