# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Service 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import ServiceForm
import cmdb_log

@login_required
def service_get(request):
    if request.method == 'GET':
        objects = Service.objects.all()
        context = {'objects':objects}
        return render(request,'object_service_list.html',context)

@permission_required('cmdb.change_service',raise_exception=True)
@login_required
def service_add(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Service_Name,data)
        return redirect('object_service_get')
    return render(request, 'object_service_form.html', {'form':form})

@permission_required('cmdb.change_service',raise_exception=True)
@login_required
def service_edit(request,pk):
    object = get_object_or_404(Service,pk=pk)
    object_data = object.__dict__.copy()
    form = ServiceForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Service_Name'],message)
        return redirect('object_service_get')
    return render(request,'object_service_form.html', {'form':form})

@permission_required('cmdb.change_service',raise_exception=True)
@login_required
def service_delete(request,pk):
    object= get_object_or_404(Service,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(service=object.id) or HostVirtual.objects.filter(service=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Service_Name,object_data)
        return redirect('object_service_get')
    return render(request,'object_service_confirm_delete.html', {'object':object})
