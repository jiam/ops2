# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import RAID,HostPhysical 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import RAIDForm
import cmdb_log

@login_required
def raid_get(request):
    if request.method == 'GET':
        objects = RAID.objects.all()
        context = {'objects':objects}
        return render(request,'object_raid_list.html',context)

@permission_required('cmdb.change_raid',raise_exception=True)
@login_required
def raid_add(request):
    form = RAIDForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.RAID_Type,data)
        return redirect('object_raid_get')
    return render(request, 'object_raid_form.html', {'form':form})

@permission_required('cmdb.change_raid',raise_exception=True)
@login_required
def raid_edit(request,pk):
    object = get_object_or_404(RAID,pk=pk)
    object_data = object.__dict__.copy()
    form = RAIDForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['RAID_Type'],message)
        return redirect('object_raid_get')
    return render(request,'object_raid_form.html', {'form':form})

@permission_required('cmdb.change_raid',raise_exception=True)
@login_required
def raid_delete(request,pk):
    object= get_object_or_404(RAID,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(raid=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.RAID_Type,object_data)
        return redirect('object_raid_get')
    return render(request,'object_raid_confirm_delete.html', {'object':object})
