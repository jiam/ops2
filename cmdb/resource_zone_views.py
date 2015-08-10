# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Zone,HostPhysical 
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required,permission_required
from form import ZoneForm
import cmdb_log
import json

@login_required
def zone_get(request):
    if request.method == 'GET':
        objects = Zone.objects.all()
        context = {'objects':objects}
        return render(request,'resource_zone_list.html',context)
@permission_required('cmdb.change_zone',raise_exception=True)
@login_required
def zone_add(request):
    form = ZoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Zone_Name,data)
        return redirect('resource_zone_get')
    return render(request, 'resource_zone_form.html', {'form':form})

@permission_required('cmdb.change_zone',raise_exception=True)
@login_required
def zone_edit(request,pk):
    object = get_object_or_404(Zone,pk=pk)
    object_data = object.__dict__.copy()
    form = ZoneForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = form.cleaned_data
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Zone_Name'],message)
        return redirect('resource_zone_get')
    return render(request,'resource_zone_form.html', {'form':form})

@permission_required('cmdb.change_zone',raise_exception=True)
@login_required
def zone_delete(request,pk):
    object= get_object_or_404(Zone,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(zone=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Zone_Name,object_data)
        return redirect('resource_zone_get')
    return render(request,'resource_zone_confirm_delete.html', {'object':object})


@login_required
@csrf_exempt
def ajax_zone_get(request):
    response = {}
    data = []
    id_idc = int(request.POST['id_idc'])
    if id_idc:
        zones =  Zone.objects.filter(idc=id_idc)
        for zone in zones:
            id_zone = zone.id
            data.append({'id':id_zone,'name':zone.Zone_Name})
        response = {'item_list':data}
        return HttpResponse(json.dumps(response))
    return HttpResponse(json.dumps(response))

