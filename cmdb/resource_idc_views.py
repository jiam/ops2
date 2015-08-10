# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import IDC,HostPhysical 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import IDCForm
import cmdb_log

@login_required
def idc_get(request):
    if request.method == 'GET':
        objects = IDC.objects.all()
        context = {'objects':objects}
        return render(request,'resource_idc_list.html',context)
@permission_required('cmdb.change_idc',raise_exception=True)
@login_required
def idc_add(request):
    form = IDCForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.IDC_Name,data)
        return redirect('resource_idc_get')
    return render(request, 'resource_idc_form.html', {'form':form})

@permission_required('cmdb.change_idc',raise_exception=True)
@login_required
def idc_edit(request,pk):
    object = get_object_or_404(IDC,pk=pk)
    resource_data = object.__dict__.copy()
    form = IDCForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,resource_data)
        cmdb_log.log_change(request,i,form_data['IDC_Name'],message)
        return redirect('resource_idc_get')
    return render(request,'resource_idc_form.html', {'form':form})

@permission_required('cmdb.change_idc',raise_exception=True)
@login_required
def idc_delete(request,pk):
    object= get_object_or_404(IDC,pk=pk)
    resource_data = object.__dict__.copy()
    if HostPhysical.objects.filter(idc=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.IDC_Name,resource_data)
        return redirect('resource_idc_get')
    return render(request,'resource_idc_confirm_delete.html', {'object':object})
