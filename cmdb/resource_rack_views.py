# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Rack,HostPhysical 
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required,permission_required
from form import RackForm
import cmdb_log
import json

@login_required
def rack_get(request):
    if request.method == 'GET':
        objects = Rack.objects.all()
        context = {'objects':objects}
        return render(request,'resource_rack_list.html',context)

@permission_required('cmdb.change_rack',raise_exception=True)
@login_required
def rack_add(request):
    form = RackForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Rack_Name,data)
        return redirect('resource_rack_get')
    return render(request, 'resource_rack_form.html', {'form':form})

@permission_required('cmdb.change_rack',raise_exception=True)
@login_required
def rack_edit(request,pk):
    object = get_object_or_404(Rack,pk=pk)
    resource_data = object.__dict__.copy()
    form = RackForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,resource_data)
        cmdb_log.log_change(request,i,form_data['Rack_Name'],message)
        return redirect('resource_rack_get')
    return render(request,'resource_rack_form.html', {'form':form})

@permission_required('cmdb.change_rack',raise_exception=True)
@login_required
def rack_delete(request,pk):
    object= get_object_or_404(Rack,pk=pk)
    resource_data = object.__dict__.copy()
    if HostPhysical.objects.filter(rack=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Rack_Name,resource_data)
        return redirect('resource_rack_get')
    return render(request,'resource_rack_confirm_delete.html', {'object':object})


@login_required
@csrf_exempt
def ajax_rack_get(request):
    response = {}
    data = []
    id_idc = int(request.POST['id_idc'])
    if id_idc:
        racks =  Rack.objects.filter(idc=id_idc)
        for rack in racks:
            id_rack = rack.id
            data.append({'id':id_rack,'name':rack.Rack_Name})
        response = {'item_list':data}
        return HttpResponse(json.dumps(response))
    return HttpResponse(json.dumps(response))
