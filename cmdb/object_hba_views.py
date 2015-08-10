# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import HBA,HostPhysical
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import HBAForm
import cmdb_log

@login_required
def hba_get(request):
    if request.method == 'GET':
        objects = HBA.objects.all()
        context = {'objects':objects}
        return render(request,'object_hba_list.html',context)

@permission_required('cmdb.change_hba',raise_exception=True)
@login_required
def hba_add(request):
    form = HBAForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.HBA_Type,data)
        return redirect('object_hba_get')
    return render(request, 'object_hba_form.html', {'form':form})

@permission_required('cmdb.change_hba',raise_exception=True)
@login_required
def hba_edit(request,pk):
    object = get_object_or_404(HBA,pk=pk)
    object_data = object.__dict__.copy()
    form = HBAForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['HBA_Type'],message)
        return redirect('object_hba_get')
    return render(request,'object_hba_form.html', {'form':form})

@permission_required('cmdb.change_hba',raise_exception=True)
@login_required
def hba_delete(request,pk):
    object= get_object_or_404(HBA,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(hba=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.HBA_Type,object_data)
        return redirect('object_hba_get')
    return render(request,'object_hba_confirm_delete.html', {'object':object})
