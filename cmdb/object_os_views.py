# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import OS,HostPhysical,HostVirtual
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import OSForm
import cmdb_log

@login_required
def os_get(request):
    if request.method == 'GET':
        objects = OS.objects.all()
        context = {'objects':objects}
        return render(request,'object_os_list.html',context)

@permission_required('cmdb.change_os',raise_exception=True)
@login_required
def os_add(request):
    form = OSForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.OS_Name,data)
        return redirect('object_os_get')
    return render(request, 'object_os_form.html', {'form':form})

@permission_required('cmdb.change_os',raise_exception=True)
@login_required
def os_edit(request,pk):
    object = get_object_or_404(OS,pk=pk)
    object_data = object.__dict__.copy()
    form = OSForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['OS_Name'],message)
        return redirect('object_os_get')
    return render(request,'object_os_form.html', {'form':form})

@permission_required('cmdb.change_os',raise_exception=True)
@login_required
def os_delete(request,pk):
    object= get_object_or_404(OS,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(os=object.id) or HostVirtual.objects.filter(os=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.OS_Name,object_data)
        return redirect('object_os_get')
    return render(request,'object_os_confirm_delete.html', {'object':object})
