# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from cmdb.models import Model,HostPhysical 
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required,permission_required
from form import ModelsForm
import cmdb_log
import json

@login_required
def model_get(request):
    if request.method == 'GET':
        objects = Model.objects.all().order_by('vendor')
        context = {'objects':objects}
        return render(request,'object_model_list.html',context)

@permission_required('cmdb.change_model',raise_exception=True)
@login_required
def model_add(request):
    form = ModelsForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.Model_Name,data)
        return redirect('object_model_get')
    return render(request, 'object_model_form.html', {'form':form})

@permission_required('cmdb.change_model',raise_exception=True)
@login_required
def model_edit(request,pk):
    object = get_object_or_404(Model,pk=pk)
    object_data = object.__dict__.copy()
    form = ModelsForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = i.__dict__.copy()
        form_data.pop('_vendor_cache')
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['Model_Name'],message)
        return redirect('object_model_get')
        #return HttpResponse(form_data)
    return render(request,'object_model_form.html', {'form':form})

@permission_required('cmdb.change_model',raise_exception=True)
@login_required
def model_delete(request,pk):
    object= get_object_or_404(Model,pk=pk)
    object_data = object.__dict__.copy()
    if HostPhysical.objects.filter(model=object.id):
        return render(request,'deny_delete.html')
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.Model_Name,object_data)
        return redirect('object_model_get')
    return render(request,'object_model_confirm_delete.html', {'object':object})

@login_required
@csrf_exempt
def ajax_model_get(request):
    response = {}
    data = []
    id_vendor = int(request.POST['id_vendor'])
    if id_vendor:
        models =  Model.objects.filter(vendor=id_vendor)
        for model in models:
            id_model = model.id
            data.append({'id':id_model,'name':model.Model_Name})
        response = {'item_list':data}
        return HttpResponse(json.dumps(response))
    return HttpResponse(json.dumps(response))
