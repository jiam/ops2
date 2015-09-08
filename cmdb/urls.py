from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import views
import dashboard_views
import object_vendor_views
import object_cpu_views
import object_memory_views
import object_disk_views
import object_hba_views
import object_pcie_views
import object_nic_views
import object_raid_views
import object_model_views
import object_os_views
import object_kernel_views
import object_service_views
import object_department_views
import host_physical_views
import host_virtual_views
import accessories_memory_views
import accessories_disk_views
import resource_idc_views
import resource_zone_views
import resource_rack_views
import search_views
import api_views
import application_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/', include('haystack.urls')),
    url(r'^search/', search_views.search),
    url(r'^api/token$', api_views.get_token),
    url(r'^api/idc/get$', api_views.get_idc),
    url(r'^api/vendor/get$', api_views.get_vendor),
    url(r'^api/model/get$', api_views.get_model),
    url(r'^api/os/get$', api_views.get_os),
    url(r'^api/kernel/get$', api_views.get_kernel),
    url(r'^api/department/get$', api_views.get_department),
    url(r'^api/service/get$', api_views.get_service),
    url(r'^api/zone/get$', api_views.get_zone),
    url(r'^api/rack/get$', api_views.get_rack),
    url(r'^api/cpu/get$', api_views.get_cpu),
    url(r'^api/disk/get$', api_views.get_disk),
    url(r'^api/memory/get$', api_views.get_memory),
    url(r'^api/raid/get$', api_views.get_raid),
    url(r'^api/hba/get$', api_views.get_hba),
    url(r'^api/pcie/get$', api_views.get_pcie),
    url(r'^api/nic/get$', api_views.get_nic),
    url(r'^api/host/physical/add$', api_views.host_physical_add),
    url(r'^api/host/physical/update$', api_views.host_physical_update),
    url(r'^api/host/physical/get$', api_views.host_physical_get),
    url(r'^api/host/virtual/add$', api_views.host_virtual_add),
    url(r'^api/host/virtual/update$', api_views.host_virtual_update),
    url(r'^api/host/virtual/get$', api_views.host_virtual_get),
    url(r'^api/application/add$', api_views.application_add),
    url(r'^api/application/get$', api_views.application_get),
    url(r'^api/search$', api_views.search),
    url(r'^$',views.index),
    url(r'^user$',views.user),
    url(r'^user/info$',views.get_userinfo),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^user/changepw$',views.changepw),
    url(r'^loginlog/get$',views.get_login_log),
    url(r'^loginlog/search$',views.search_login_log),
    url(r'^oplog/get$',views.get_op_log),
    url(r'^oplog/detail/(?P<pk>\d+)$', views.get_op_detail,name='get_op_detail'),
    url(r'^oplog/search$',views.search_op_log),
    url(r'^getuserinfo$',views.get_userinfo),
    url(r'^dashboard$',dashboard_views.dashboard),
    url(r'^dashboard/host$',dashboard_views.dashboard_host),
    url(r'^dashboard/os$',dashboard_views.dashboard_os),
    url(r'^dashboard/vendor$',dashboard_views.dashboard_vendor),
    url(r'^object/department/get$', object_department_views.department_get,name='object_department_get'),
    url(r'^object/department/add$', object_department_views.department_add),
    url(r'^object/department/edit/(?P<pk>\d+)$', object_department_views.department_edit,name='object_department_edit'),
    url(r'^object/department/delete/(?P<pk>\d+)$', object_department_views.department_delete,name='object_department_delete'),
    url(r'^object/service/get$', object_service_views.service_get,name='object_service_get'),
    url(r'^object/service/add$', object_service_views.service_add),
    url(r'^object/service/edit/(?P<pk>\d+)$', object_service_views.service_edit,name='object_service_edit'),
    url(r'^object/service/delete/(?P<pk>\d+)$', object_service_views.service_delete,name='object_service_delete'),
    url(r'^object/vendor/get$', object_vendor_views.vendor_get,name='object_vendor_get'),
    url(r'^object/vendor/add$', object_vendor_views.vendor_add),
    url(r'^object/vendor/edit/(?P<pk>\d+)$', object_vendor_views.vendor_edit,name='object_vendor_edit'),
    url(r'^object/vendor/delete/(?P<pk>\d+)$', object_vendor_views.vendor_delete,name='object_vendor_delete'),
    url(r'^object/model/get$', object_model_views.model_get,name='object_model_get'),
    url(r'^object/model/ajax/get$', object_model_views.ajax_model_get),
    url(r'^object/model/add$', object_model_views.model_add),
    url(r'^object/model/edit/(?P<pk>\d+)$', object_model_views.model_edit,name='object_model_edit'),
    url(r'^object/model/delete/(?P<pk>\d+)$', object_model_views.model_delete,name='object_model_delete'),
    url(r'^object/cpu/get$', object_cpu_views.cpu_get,name='object_cpu_get'),
    url(r'^object/cpu/add$', object_cpu_views.cpu_add),
    url(r'^object/cpu/edit/(?P<pk>\d+)$', object_cpu_views.cpu_edit,name='object_cpu_edit'),
    url(r'^object/cpu/delete/(?P<pk>\d+)$', object_cpu_views.cpu_delete,name='object_cpu_delete'),
    url(r'^object/memory/get$', object_memory_views.memory_get,name='object_memory_get'),
    url(r'^object/memory/add$', object_memory_views.memory_add),
    url(r'^object/memory/edit/(?P<pk>\d+)$', object_memory_views.memory_edit,name='object_memory_edit'),
    url(r'^object/memory/delete/(?P<pk>\d+)$', object_memory_views.memory_delete,name='object_memory_delete'),
    url(r'^object/disk/get$', object_disk_views.disk_get,name='object_disk_get'),
    url(r'^object/disk/add$', object_disk_views.disk_add),
    url(r'^object/disk/edit/(?P<pk>\d+)$', object_disk_views.disk_edit,name='object_disk_edit'),
    url(r'^object/disk/delete/(?P<pk>\d+)$', object_disk_views.disk_delete,name='object_disk_delete'),
    url(r'^object/raid/get$', object_raid_views.raid_get,name='object_raid_get'),
    url(r'^object/raid/add$', object_raid_views.raid_add),
    url(r'^object/raid/edit/(?P<pk>\d+)$', object_raid_views.raid_edit,name='object_raid_edit'),
    url(r'^object/raid/delete/(?P<pk>\d+)$', object_raid_views.raid_delete,name='object_raid_delete'),
    url(r'^object/hba/get$', object_hba_views.hba_get,name='object_hba_get'),
    url(r'^object/hba/add$', object_hba_views.hba_add),
    url(r'^object/hba/edit/(?P<pk>\d+)$', object_hba_views.hba_edit,name='object_hba_edit'),
    url(r'^object/hba/delete/(?P<pk>\d+)$', object_hba_views.hba_delete,name='object_hba_delete'),
    url(r'^object/pcie/get$', object_pcie_views.pcie_get,name='object_pcie_get'),
    url(r'^object/pcie/add$', object_pcie_views.pcie_add),
    url(r'^object/pcie/edit/(?P<pk>\d+)$', object_pcie_views.pcie_edit,name='object_pcie_edit'),
    url(r'^object/pcie/delete/(?P<pk>\d+)$', object_pcie_views.pcie_delete,name='object_pcie_delete'),
    url(r'^object/nic/get$', object_nic_views.nic_get,name='object_nic_get'),
    url(r'^object/nic/add$', object_nic_views.nic_add),
    url(r'^object/nic/edit/(?P<pk>\d+)$', object_nic_views.nic_edit,name='object_nic_edit'),
    url(r'^object/nic/delete/(?P<pk>\d+)$', object_nic_views.nic_delete,name='object_nic_delete'),
    url(r'^object/os/get$', object_os_views.os_get,name='object_os_get'),
    url(r'^object/os/add$', object_os_views.os_add),
    url(r'^object/os/edit/(?P<pk>\d+)$', object_os_views.os_edit,name='object_os_edit'),
    url(r'^object/os/delete/(?P<pk>\d+)$', object_os_views.os_delete,name='object_os_delete'),
    url(r'^object/kernel/get$', object_kernel_views.kernel_get,name='object_kernel_get'),
    url(r'^object/kernel/add$', object_kernel_views.kernel_add),
    url(r'^object/kernel/edit/(?P<pk>\d+)$', object_kernel_views.kernel_edit,name='object_kernel_edit'),
    url(r'^object/kernel/delete/(?P<pk>\d+)$', object_kernel_views.kernel_delete,name='object_kernel_delete'),
    url(r'^host/physical/get$', host_physical_views.physical_get,name='host_physical_get'),
    url(r'^host/physical/search$', host_physical_views.physical_search,name='host_physical_search'),
    url(r'^host/physical/add$', host_physical_views.physical_add),
    url(r'^host/physical/edit/(?P<pk>\d+)$', host_physical_views.physical_edit,name='host_physical_edit'),
    url(r'^host/physical/detail/(?P<pk>\d+)$', host_physical_views.physical_detail,name='host_physical_detail'),
    url(r'^host/physical/delete/(?P<pk>\d+)$', host_physical_views.physical_delete,name='host_physical_delete'),
    url(r'^host/virtual/get$', host_virtual_views.virtual_get,name='host_virtual_get'),
    url(r'^host/virtual/search$', host_virtual_views.virtual_search,name='host_virtual_search'),
    url(r'^host/virtual/add$', host_virtual_views.virtual_add),
    url(r'^host/virtual/edit/(?P<pk>\d+)$', host_virtual_views.virtual_edit,name='host_virtual_edit'),
    url(r'^host/virtual/detail/(?P<pk>\d+)$', host_virtual_views.virtual_detail,name='host_virtual_detail'),
    url(r'^host/virtual/delete/(?P<pk>\d+)$', host_virtual_views.virtual_delete,name='host_virtual_delete'),
    url(r'^accessories/memory/add$', accessories_memory_views.memory_add),
    url(r'^accessories/memory/get$', accessories_memory_views.memory_get,name='accessories_memory_get'),
    url(r'^accessories/memory/search$', accessories_memory_views.memory_search,name='accessories_memory_search'),
    url(r'^accessories/memory/eidt/(?P<pk>\d+)$', accessories_memory_views.memory_edit,name='accessories_memory_edit'),
    url(r'^accessories/memory/delete/(?P<pk>\d+)$', accessories_memory_views.memory_delete,name='accessories_memory_delete'),
    url(r'^accessories/disk/add$', accessories_disk_views.disk_add),
    url(r'^accessories/disk/get$', accessories_disk_views.disk_get,name='accessories_disk_get'),
    url(r'^accessories/disk/search$', accessories_disk_views.disk_search,name='accessories_disk_search'),
    url(r'^accessories/disk/eidt/(?P<pk>\d+)$', accessories_disk_views.disk_edit,name='accessories_disk_edit'),
    url(r'^accessories/disk/delete/(?P<pk>\d+)$', accessories_disk_views.disk_delete,name='accessories_disk_delete'),
    url(r'^resource/idc/add$', resource_idc_views.idc_add),
    url(r'^resource/idc/get$', resource_idc_views.idc_get,name='resource_idc_get'),
    url(r'^resource/idc/eidt/(?P<pk>\d+)$', resource_idc_views.idc_edit,name='resource_idc_edit'),
    url(r'^resource/idc/delete/(?P<pk>\d+)$', resource_idc_views.idc_delete,name='resource_idc_delete'),
    url(r'^resource/zone/add$', resource_zone_views.zone_add),
    url(r'^resource/zone/get$', resource_zone_views.zone_get,name='resource_zone_get'),
    url(r'^resource/zone/ajax/get$', resource_zone_views.ajax_zone_get),
    url(r'^resource/zone/eidt/(?P<pk>\d+)$', resource_zone_views.zone_edit,name='resource_zone_edit'),
    url(r'^resource/zone/delete/(?P<pk>\d+)$', resource_zone_views.zone_delete,name='resource_zone_delete'),
    url(r'^resource/rack/add$', resource_rack_views.rack_add),
    url(r'^resource/rack/get$', resource_rack_views.rack_get,name='resource_rack_get'),
    url(r'^resource/rack/ajax/get$', resource_rack_views.ajax_rack_get),
    url(r'^resource/rack/eidt/(?P<pk>\d+)$', resource_rack_views.rack_edit,name='resource_rack_edit'),
    url(r'^resource/rack/delete/(?P<pk>\d+)$', resource_rack_views.rack_delete,name='resource_rack_delete'),
    url(r'^application/add$', application_views.application_add),
    url(r'^application/get$', application_views.application_get,name='application_get'),
    url(r'^application/search$', application_views.application_search,name='application_search'),
    url(r'^application/(?P<pk>\d+)$', application_views.application_edit,name='application_edit'),
    url(r'^application/delete/(?P<pk>\d+)$', application_views.application_delete,name='application_delete'),
    url(r'^application/detail/(?P<pk>\d+)$', application_views.application_detail,name='application_detail'),
    url(r'^application/export$', application_views.application_export,name='application_export'),
)
