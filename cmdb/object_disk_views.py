# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Disk,HostPhysical 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import DiskForm
import cmdb_log

@login_required
def disk_get(request):
    if request.method == 'GET':
        objects = Disk.objects.all()
        context = {'objects':objects}
        return render(request,'object_disk_list.html',context)

@permission_required('cmdb.change_disk',raise_exception=True)
@login_required
def disk_add(request):
    form = DiskForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Disk_Type,data)
        return redirect('object_disk_get')
    return render(request, 'object_disk_form.html', {'form':form})

@permission_required('cmdb.change_disk',raise_exception=True)
@login_required
def disk_edit(request,pk):
    object = get_object_or_404(Disk,pk=pk)
    object_data = object.__dict__.copy()
    form = DiskForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Disk_Type'],message)
        return redirect('object_disk_get')
    return render(request,'object_disk_form.html', {'form':form})

@permission_required('cmdb.change_disk',raise_exception=True)
@login_required
def disk_delete(request,pk):
    object= get_object_or_404(Disk,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(disk=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Disk_Type,object_data)
        return redirect('object_disk_get')
    return render(request,'object_disk_confirm_delete.html', {'object':object})
