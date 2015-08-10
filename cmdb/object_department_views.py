# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Department,HostPhysical,HostVirtual
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import DepartmentForm
import cmdb_log

@login_required
def department_get(request):
    if request.method == 'GET':
        objects = Department.objects.all()
        context = {'objects':objects}
        return render(request,'object_department_list.html',context)

@permission_required('cmdb.change_department',raise_exception=True)
@login_required
def department_add(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Department_Name,data)
        return redirect('object_department_get')
    return render(request, 'object_department_form.html', {'form':form})

@permission_required('cmdb.change_department',raise_exception=True)
@login_required
def department_edit(request,pk):
    object = get_object_or_404(Department,pk=pk)
    object_data = object.__dict__.copy()
    form = DepartmentForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Department_Name'],message)
        return redirect('object_department_get')
    return render(request,'object_department_form.html', {'form':form})

@permission_required('cmdb.change_department',raise_exception=True)
@login_required
def department_delete(request,pk):
    object= get_object_or_404(Department,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(department=object.id) or HostVirtual.objects.filter(department=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Department_Name,object_data)
        return redirect('object_department_get')
    return render(request,'object_department_confirm_delete.html', {'object':object})
