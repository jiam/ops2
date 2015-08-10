# -*- coding: utf-8 -*-
from __future__ import division
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Count
from cmdb.models import *
import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
@login_required    
def dashboard(request):
    return render(request,'dashboard.html',{})
def dashboard_host(request):
    physicals = HostPhysical.objects.count()
    virtuals = HostVirtual.objects.count()
    data = {'x':["物理主机","虚拟主机"],'y':[physicals,virtuals]}
    j_data = json.dumps(data)
    return HttpResponse(j_data)

@login_required    
def dashboard_os(request):
    data = []
    oss = list(HostVirtual.objects.values('os').annotate(dcount=Count('os')))
    count = len(HostVirtual.objects.all())
    for os in  oss:
        os_id = os['os']
        os_name =  OS.objects.get(id=os_id).OS_Name
        #percent = os['dcount'] / count
        percent = os['dcount']
        data.append([os_name, percent])
    j_data = json.dumps(data)
    return HttpResponse(j_data)
        
        
def dashboard_vendor(request):
    data = []
    vendors = list(HostPhysical.objects.values('vendor').annotate(dcount=Count('vendor')))
    count = HostPhysical.objects.count()
    for vendor in  vendors:
        vendor_id = vendor['vendor']
        vendor_name =  Vendor.objects.get(id=vendor_id).Vendor_Name
        #percent = os['dcount'] / count
        percent = vendor['dcount']
        data.append([vendor_name, percent])
    j_data = json.dumps(data)
    return HttpResponse(j_data)

    
     
