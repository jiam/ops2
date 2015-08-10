# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Accessories_Disk 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import Accessories_DiskForm
import cmdb_log

@login_required
def disk_get(request):
    if request.method == 'GET':
        objects = Accessories_Disk.objects.all()
        context = {'objects':objects}
        return render(request,'accessories_disk_list.html',context)

@permission_required('cmdb.change_accessories_disk',raise_exception=True)
@login_required
def disk_add(request):
    form = Accessories_DiskForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.SN,data)
        return redirect('accessories_disk_get')
    return render(request, 'accessories_disk_form.html', {'form':form})

@permission_required('cmdb.change_accessories_disk',raise_exception=True)
@login_required
def disk_edit(request,pk):
    object = get_object_or_404(Accessories_Disk,pk=pk)
    object_data = object.__dict__.copy()
    form = Accessories_DiskForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['SN'],message)
        return redirect('accessories_disk_get')
    return render(request,'accessories_disk_form.html', {'form':form})

@permission_required('cmdb.change_accessories_disk',raise_exception=True)
@login_required
def disk_delete(request,pk):
    object= get_object_or_404(Accessories_Disk,pk=pk)
    object_data = object.__dict__.copy()
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.SN,object_data)
        return redirect('accessories_disk_get')
    return render(request,'accessories_disk_confirm_delete.html', {'object':object})
