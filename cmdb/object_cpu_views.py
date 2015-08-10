# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import CPU,HostPhysical
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import CPUForm
import cmdb_log

@login_required
def cpu_get(request):
    if request.method == 'GET':
        objects = CPU.objects.all()
        context = {'objects':objects}
        return render(request,'object_cpu_list.html',context)

@permission_required('cmdb.change_cpu',raise_exception=True)
@login_required
def cpu_add(request):
    form = CPUForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.CPU_Type,data)
        return redirect('object_cpu_get')
    return render(request, 'object_cpu_form.html', {'form':form})

@permission_required('cmdb.change_cpu',raise_exception=True)
@login_required
def cpu_edit(request,pk):
    object = get_object_or_404(CPU,pk=pk)
    object_data = object.__dict__.copy()
    form = CPUForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['CPU_Type'],message)
        return redirect('object_cpu_get')
    return render(request,'object_cpu_form.html', {'form':form})

@permission_required('cmdb.change_cpu',raise_exception=True)
@login_required
def cpu_delete(request,pk):
    object= get_object_or_404(CPU,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(cpu=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.CPU_Type,object_data)
        return redirect('object_cpu_get')
    return render(request,'object_cpu_confirm_delete.html', {'object':object})
