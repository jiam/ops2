# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from cmdb.models import HostPhysical 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required,permission_required
from form import HostPhysicalForm
import cmdb_log
import json

@login_required
def physical_get(request):
    if request.method == 'GET':
        objects_list = HostPhysical.objects.all().order_by('vendor')
        num = objects_list.count()
        paginator = Paginator(objects_list,15)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        context = {'objects':objects,'total':num}
        return render(request,'host_physical_list.html',context)

@permission_required('cmdb.change_hostphysical',raise_exception=True)
@login_required
def physical_add(request):
    form = HostPhysicalForm(request.POST or None)
    if form.is_valid():
        form.save()
        i = form.instance
        data = form.cleaned_data
        cmdb_log.log_addition(request,i,i.HostName,data)
        return redirect('host_physical_get')
    #else:
    #    return HttpResponse(form.errors)
    return render(request, 'host_physical_form.html', {'form':form})

@permission_required('cmdb.change_hostphysical',raise_exception=True)
@login_required
def physical_edit(request,pk):
    object = get_object_or_404(HostPhysical,pk=pk)
    object_data = model_to_dict(object)
    form = HostPhysicalForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        i = form.instance
        form_data = model_to_dict(i)
        message = cmdb_log.cmp(form_data,object_data)
        cmdb_log.log_change(request,i,form_data['HostName'],message)
        return redirect('host_physical_get')
    return render(request,'host_physical_form.html', {'form':form})

@permission_required('cmdb.change_hostphysical',raise_exception=True)
@login_required
def physical_delete(request,pk):
    object= get_object_or_404(HostPhysical,pk=pk)
    object_data = object.__dict__.copy()
    if request.method=='POST':
        object.delete()
        cmdb_log.log_deletion(request,object,object.HostName,object_data)
        return redirect('host_physical_get')
    return render(request,'host_physical_confirm_delete.html', {'object':object})


@login_required
def physical_detail(request,pk):
    object = get_object_or_404(HostPhysical,pk=pk)
    return render(request,'host_physical_detail.html', {'object':object})
