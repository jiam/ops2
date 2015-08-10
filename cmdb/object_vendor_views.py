# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Vendor,HostPhysical
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import VendorForm
import cmdb_log

@login_required
def vendor_get(request):
    if request.method == 'GET':
        objects = Vendor.objects.all()
        context = {'objects':objects}
        return render(request,'object_vendor_list.html',context)

@permission_required('cmdb.change_vendor',raise_exception=True)
@login_required
def vendor_add(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Vendor_Name,data)
        return redirect('object_vendor_get')
    return render(request, 'object_vendor_form.html', {'form':form})

@permission_required('cmdb.change_vendor',raise_exception=True)
@login_required
def vendor_edit(request,pk):
    object = get_object_or_404(Vendor,pk=pk)
    object_data = object.__dict__.copy()
    form = VendorForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Vendor_Name'],message)
        return redirect('object_vendor_get')
    return render(request,'object_vendor_form.html', {'form':form})

@permission_required('cmdb.change_vendor',raise_exception=True)
@login_required
def vendor_delete(request,pk):
    object= get_object_or_404(Vendor,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(vendor=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Vendor_Name,object_data)
        return redirect('object_vendor_get')
    return render(request,'object_vendor_confirm_delete.html', {'object':object})
