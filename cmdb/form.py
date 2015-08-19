#  -*- coding: utf8 -*-
from django import forms
from django.forms import ModelForm,TextInput,ModelChoiceField,extras,Textarea
from cmdb.models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'账号',
        'required':'True',
        'autofocus':'True'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'密码',
        'required':'True',
        'autofocus':'True'}))
 
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['Department_Name', 'Department_Contact']
        labels = {
            'Department_Name':'部门名称',
            'Department_Contact':'部门接口人'
        }
        widgets = {
            'Department_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'Department_Contact':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'})
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['Service_Name']
        labels = {
            'Service_Name':'业务名称',
        }
        widgets = {
            'Service_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['Vendor_Name']
        labels = {
            'Vendor_Name':'厂商名称',
        }
        widgets = {
            'Vendor_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }


class ModelsForm(ModelForm):
    vendor = ModelChoiceField(label='所属厂商',
        queryset=Vendor.objects.all(),to_field_name="Vendor_Name",
        widget=forms.Select(attrs={
            'class':'form-control'}))
    class Meta:
        model = Model
        fields = ['Model_Name', 'vendor']
        labels = {
            'Model_Name':'型号名称',
        }
        widgets = {
            'Model_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }


class CPUForm(ModelForm):
    class Meta:
        model = CPU
        fields = ['CPU_Type', 'CPU_Cores','CPU_Logical_Cores','CPU_Frequency']
        labels = {
            'CPU_Type':'CPU型号',
            'CPU_Frequency':'CPU频率',
            'CPU_Cores':'物理核数',
            'CPU_Logical_Cores':'逻辑核数'
        }
        widgets = {
            'CPU_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'CPU_Cores':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'CPU_Logical_Cores':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'CPU_Frequency':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'})
        }

class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ['Memory_Type']
        labels = {
            'Memory_Type':'内存型号',
        }
        widgets = {
            'Memory_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class DiskForm(ModelForm):
    class Meta:
        model = Disk
        fields = ['Disk_Type']
        labels = {
            'Disk_Type':'内存型号',
        }
        widgets = {
            'Disk_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class RAIDForm(ModelForm):
    CHOICES = ((0,'无'),(1,'有'))
    RAID_Battery = forms.ChoiceField(label='RAID电池',widget=forms.Select(),choices=CHOICES)
    class Meta:
        model = RAID
        fields = ['RAID_Type', 'RAID_Cache','RAID_Battery']
        labels = {
            'RAID_Type':'RAID型号',
            'RAID_Cache':'RAID缓存'
        }
        widgets = {
            'RAID_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'RAID_Cache':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class HBAForm(ModelForm):
    class Meta:
        model = HBA
        fields = ['HBA_Type']
        labels = {
            'HBA_Type':'HBA型号',
        }
        widgets = {
            'HBA_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class PCIEForm(ModelForm):
    class Meta:
        model = PCIE
        fields = ['PCIE_Type']
        labels = {
            'PCIE_Type':'PCIE型号',
        }
        widgets = {
            'PCIE_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class NICForm(ModelForm):
    class Meta:
        model = NIC
        fields = ['NIC_Type']
        labels = {
            'NIC_Type':'NIC型号',
        }
        widgets = {
            'NIC_Type':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class OSForm(ModelForm):
    class Meta:
        model = OS
        fields = ['OS_Name']
        labels = {
            'OS_Name':'操作系统',
        }
        widgets = {
            'OS_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class KernelForm(ModelForm):
    class Meta:
        model = Kernel
        fields = ['Kernel_Name']
        labels = {
            'Kernel_Name':'内核版本',
        }
        widgets = {
            'Kernel_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class HostPhysicalForm(ModelForm):
    HostName = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':5,
        'placeholder':'必填',
        'required':'True',
        'autofocus':'True'}))
    UseInfo = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':100,
        'size':51,
        'placeholder':'必填',
        'required':'True',}))
    User = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':5,
        'placeholder':'必填',
        'required':'True',}))
    Manage_IP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        'placeholder':'必填',
        'required':'True',}))
    RAC_IP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        }),
        required=False)
    VIP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        }),
        required=False)
    NAS_IP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        }),
        required=False)
    Memory_Size = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':3,
        'placeholder':'必填',
        'required':'True',}))
    Disk_Size = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':3,
        'placeholder':'必填',
        'required':'True',}))
    Rack_Position = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':4,
        'placeholder':'必填',
        'required':'True',}))
    Asset_SN = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        'placeholder':'必填',
        'required':'True',}))
    SN = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        'placeholder':'必填',
        'required':'True',}))
    CPU_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':2,
        }),
        initial=0)
    Memory_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':2,
        }),
        initial=0)
    Disk_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':2,
        }),
        initial=0)
    HBA_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':2,
        }),
        initial=0)
    PCIE_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':2,
        }),
        initial=0)
   
    NIC_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':2,
        'size':2,
        }),
        initial=0)
    Remarks = forms.CharField(widget=forms.Textarea(attrs={
        'rows':2}),
        required=False,
        )
    Change_Info = forms.CharField(widget=forms.Textarea(attrs={
        'rows':2}),
        required=False,
        )

    RAID_Battery_CHOICES = ((0,'无'),(1,'有'))
    RAID_Battery = forms.ChoiceField(label='RAID电池',widget=forms.Select(),choices=RAID_Battery_CHOICES)
    
    RAID_CHOICES = ((0,'无'),(1,'RAID 0'),(2,'RAID 1'),(3,'RAID 5'),(4,'RAID 10'),(5,'RAID 1+5'),(6,'RAID 1+10'))
    Status_CHOICES = ((0,'使用'),(1,'空闲'),(2,'故障'),(3,'备用'))
    RAID_Level = forms.ChoiceField(widget=forms.Select(),choices=RAID_CHOICES)
    Status = forms.ChoiceField(widget=forms.Select(),choices=Status_CHOICES)
    Purchasing_Time = forms.DateField(initial='2015-01-01')
    Guarantee_Time = forms.DateField(initial='2015-01-01')
    Up_Time = forms.DateField(initial='2015-01-01')
    Change_Time = forms.DateField(initial='2015-01-01')
    class Meta:
        model = HostPhysical
        #fields = ['HostName','Status','Asset_SN','vendor','model','SN']
        fields = '__all__'


class HostVirtualForm(ModelForm):
    HostName = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':5,
        'placeholder':'必填',
        'required':'True',
        'autofocus':'True'}))
    Use_Info = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':100,
        'size':51,
        'placeholder':'必填',
        'required':'True',}))
    User = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':5,
        'placeholder':'必填',
        'required':'True',}))
    Manage_IP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        'placeholder':'必填',
        'required':'True',}))
    VIP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        }),
        required=False)
    NAS_IP = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':12,
        }),
        required=False)
    Memory_Size = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':3,
        'placeholder':'必填',
        'required':'True',}))
    Disk_Size = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':3,
        'placeholder':'必填',
        'required':'True',}))
    vCPU_Number = forms.CharField(widget=forms.TextInput(attrs={
        'maxlength':30,
        'size':2,
        }),
        initial=0)

    Remarks = forms.CharField(widget=forms.Textarea(attrs={
        'rows':2}),
        required=False,
        )
    Change_Info = forms.CharField(widget=forms.Textarea(attrs={
        'rows':2}),
        required=False,
        )


    Status_CHOICES = ((0,'使用'),(1,'空闲'),(2,'故障'),(3,'备用'))
    Status = forms.ChoiceField(widget=forms.Select(),choices=Status_CHOICES)
    Application_Time = forms.DateField(initial='2015-01-01')
    Use_Period = forms.DateField(initial='2015-01-01')
    Up_Time = forms.DateField(initial='2015-01-01')
    Change_Time = forms.DateField(initial='2015-01-01')
    class Meta:
        model = HostVirtual
        #fields = ['HostName','Status','Asset_SN','vendor','model','SN']
        fields = '__all__'


class Accessories_MemoryForm(ModelForm):
    Status_CHOICES = ((0,'使用'),(1,'库存'),(2,'故障'))
    Status = forms.ChoiceField(label='状态',widget=forms.Select(),choices=Status_CHOICES)
    class Meta:
        model = Accessories_Memory
        fields = ['SN', 'Status','Memory_Type','Host_SN']
        labels = {
            'SN':'SN',
            'Memory_Type':'内存类型',
            'Host_SN':'主机SN'
        }
        widgets = {
            'SN':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'Host_SN':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'})
        }

class Accessories_DiskForm(ModelForm):
    Status_CHOICES = ((0,'使用'),(1,'库存'),(2,'故障'))
    Status = forms.ChoiceField(label='状态',widget=forms.Select(),choices=Status_CHOICES)
    class Meta:
        model = Accessories_Disk
        fields = ['SN', 'Status','Disk_Type','Host_SN']
        labels = {
            'SN':'SN',
            'Disk_Type':'内存类型',
            'Host_SN':'主机SN'
        }
        widgets = {
            'SN':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'Host_SN':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'})
        }


class IDCForm(ModelForm):
    class Meta:
        model = IDC
        fields = ['IDC_Name', 'IDC_Location','IDC_Contact','IDC_Phone','IDC_Email']
        labels = {
            'IDC_Name':'机房名称',
            'IDC_Location':'机房地址',
            'IDC_Contact':'机房联系人',
            'IDC_Phone':'联系电话',
            'IDC_Email':'邮箱地址'
        }
        widgets = {
            'IDC_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'IDC_Location':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'IDC_Contact':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'IDC_Phone':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
            'IDC_Email':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'})
        }

class ZoneForm(ModelForm):
    idc = ModelChoiceField(label='所属机房',
        queryset=IDC.objects.all(),to_field_name="IDC_Name",
        widget=forms.Select(attrs={
            'class':'form-control'}))
    class Meta:
        model = Zone 
        fields = ['Zone_Name', 'idc']
        labels = {
            'Zone_Name':'区域名称',
        }
        widgets = {
            'Zone_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }

class RackForm(ModelForm):
    idc = ModelChoiceField(label='所属机房',
        queryset=IDC.objects.all(),to_field_name="IDC_Name",
        widget=forms.Select(attrs={
            'class':'form-control'}))
    class Meta:
        model = Rack
        fields = ['Rack_Name', 'idc']
        labels = {
            'Rack_Name':'机柜名称',
        }
        widgets = {
            'Rack_Name':TextInput(attrs={
                'class':'form-control',
                'required':'True',
                'autofocus':'True'}),
        }
