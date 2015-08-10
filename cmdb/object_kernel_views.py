# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Kernel,HostPhysical,HostVirtual
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import KernelForm
import cmdb_log

@login_required
def kernel_get(request):
    if request.method == 'GET':
        objects = Kernel.objects.all()
        context = {'objects':objects}
        return render(request,'object_kernel_list.html',context)

@permission_required('cmdb.change_kernel',raise_exception=True)
@login_required
def kernel_add(request):
    form = KernelForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Kernel_Name,data)
        return redirect('object_kernel_get')
    return render(request, 'object_kernel_form.html', {'form':form})

@permission_required('cmdb.change_kernel',raise_exception=True)
@login_required
def kernel_edit(request,pk):
    object = get_object_or_404(Kernel,pk=pk)
    object_data = object.__dict__.copy()
    form = KernelForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Kernel_Name'],message)
        return redirect('object_kernel_get')
    return render(request,'object_kernel_form.html', {'form':form})

@permission_required('cmdb.change_kernel',raise_exception=True)
@login_required
def kernel_delete(request,pk):
    object= get_object_or_404(Kernel,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(kernel=object.id) or HostVirtual.objects.filter(kernel=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Kernel_Name,object_data)
        return redirect('object_kernel_get')
    return render(request,'object_kernel_confirm_delete.html', {'object':object})
