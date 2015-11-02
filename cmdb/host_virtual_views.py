# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from cmdb.models import HostVirtual 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import HostVirtualForm
import cmdb_log
import json

@login_required
def virtual_get(request):
    if request.method == 'GET':
        objects = HostVirtual.objects.all().order_by('-id')
        context = {'objects':objects}
        return render(request,'host_virtual_list.html',context)

@login_required
@permission_required('cmdb.change_hostvirtual',raise_exception=True)
def virtual_add(request):
    if request.method == 'POST':
        form = HostVirtualForm(request.POST or None)
        if form.is_valid():
            form_data = form.cleaned_data
            data = {}
            for key in form_data:
                if form_data[key]:
                    data[key] = form_data[key]
            i = HostVirtual(**data)
            i.save()
            cmdb_log.log_addition(request,i,i.HostName,data)
            return redirect('host_virtual_get')
        else:
            return HttpResponse(form.errors)
    else:
        form = HostVirtualForm()
        return render(request, 'host_virtual_add_form.html', {'form':form})

@login_required
@permission_required('cmdb.change_hostvirtual',raise_exception=True)
def virtual_edit(request,pk):
    object= get_object_or_404(HostVirtual,pk=pk)
    object_data = model_to_dict(object)
    objects = HostVirtual.objects.filter(pk=pk)
    form = HostVirtualForm(request.POST or None,instance=object)
    if form.is_valid():
        form_data = form.cleaned_data
        data = {}
        for key in  form_data:
            if form_data[key]:
                data[key] = form_data[key]
        objects.update(**data)
        new_object= get_object_or_404(HostVirtual,pk=pk)
        new_object_data = model_to_dict(new_object)
        message = cmdb_log.cmp(new_object_data,object_data)
        cmdb_log.log_change(request,new_object,form_data['HostName'],message)
        return redirect('host_virtual_get')
    return render(request,'host_virtual_update_form.html', {'form':form})

@login_required
@permission_required('cmdb.change_hostvirtual',raise_exception=True)
def virtual_delete(request,pk):
    object= get_object_or_404(HostVirtual,pk=pk)
    object_data = object.__dict__.copy()
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.HostName,object_data)
        return redirect('host_virtual_get')
    return render(request,'host_virtual_confirm_delete.html', {'object':object})


@login_required
def virtual_detail(request,pk):
    object = get_object_or_404(HostVirtual,pk=pk)
    return render(request,'host_virtual_detail.html', {'object':object})

@login_required
def virtual_search(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        search_value = request.GET['search_value']
        if search_value:
            params = { search_key+'__startswith':search_value}
            objects_list = HostVirtual.objects.filter(**params).order_by(search_key)
        else:
            objects_list = HostVirtual.objects.all().order_by(search_key)
        num = objects_list.count()
        paginator = Paginator(objects_list,15)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context = {'objects':objects,'total':num,'search_key':search_key,'search_value':search_value}
        return render(request,'host_virtual_list.html',context)
