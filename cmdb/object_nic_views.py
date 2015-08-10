# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import NIC,HostPhysical 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import NICForm
import cmdb_log

@login_required
def nic_get(request):
    if request.method == 'GET':
        objects = NIC.objects.all()
        context = {'objects':objects}
        return render(request,'object_nic_list.html',context)

@permission_required('cmdb.change_nic',raise_exception=True)
@login_required
def nic_add(request):
    form = NICForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.NIC_Type,data)
        return redirect('object_nic_get')
    return render(request, 'object_nic_form.html', {'form':form})

@permission_required('cmdb.change_nic',raise_exception=True)
@login_required
def nic_edit(request,pk):
    object = get_object_or_404(NIC,pk=pk)
    object_data = object.__dict__.copy()
    form = NICForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['NIC_Type'],message)
        return redirect('object_nic_get')
    return render(request,'object_nic_form.html', {'form':form})

@permission_required('cmdb.change_nic',raise_exception=True)
@login_required
def nic_delete(request,pk):
    object= get_object_or_404(NIC,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(nic=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.NIC_Type,object_data)
        return redirect('object_nic_get')
    return render(request,'object_nic_confirm_delete.html', {'object':object})
