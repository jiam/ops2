from django.db import models

class Vendor(models.Model):
    Vendor_Name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Vendor_Name
    def natural_key(self):
        return self.Vendor_Name

class Model(models.Model):
    Model_Name = models.CharField(max_length=30)
    vendor = models.ForeignKey(Vendor)
    def __unicode__(self):
        return self.Model_Name
    def natural_key(self):
        return self.Model_Name

class OS(models.Model):
    OS_Name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.OS_Name
    def natural_key(self):
        return self.OS_Name


class Kernel(models.Model):
    Kernel_Name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Kernel_Name
    def natural_key(self):
        return self.Kernel_Name

class CPU(models.Model):
    CPU_Type = models.CharField(max_length=30)
    CPU_Cores = models.IntegerField()
    CPU_Logical_Cores = models.IntegerField()
    CPU_Frequency = models.CharField(max_length=30)
    def __unicode__(self):
        return self.CPU_Type
    def natural_key(self):
        return self.CPU_Type
   

class Memory(models.Model):
    Memory_Type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Memory_Type
    def natural_key(self):
        return self.Memory_Type

class Disk(models.Model):
    Disk_Type = models.CharField(max_length=150)
    def __unicode__(self):
        return self.Disk_Type
    def natural_key(self):
        return self.Disk_Type

class HBA(models.Model):
    HBA_Type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.HBA_Type
    def natural_key(self):
        return self.HBA_Type

class PCIE(models.Model):
    PCIE_Type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.PCIE_Type
    def natural_key(self):
        return self.PCIE_Type

class NIC(models.Model):
    NIC_Type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.NIC_Type
    def natural_key(self):
        return self.NIC_Type

class RAID(models.Model):
    RAID_Type = models.CharField(max_length=100)
    RAID_Cache = models.CharField(max_length=30)
    RAID_Battery = models.CharField(max_length=30)
    def __unicode__(self):
        return self.RAID_Type
    def natural_key(self):
        return self.RAID_Type

class Service(models.Model):
    Service_Name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Service_Name
    def natural_key(self):
        return self.Service_Name

class IDC(models.Model):
    IDC_Name = models.CharField(max_length=50)
    IDC_Location = models.CharField(max_length=100)
    IDC_Contact = models.CharField(max_length=100)
    IDC_Phone = models.CharField(max_length=20)
    IDC_Email = models.CharField(max_length=50)
    def __unicode__(self):
        return self.IDC_Name
    def natural_key(self):
        return self.IDC_Name

class Rack(models.Model):
    Rack_Name = models.CharField(max_length=30)
    idc = models.ForeignKey(IDC)
    def __unicode__(self):
        return self.Rack_Name
    def natural_key(self):
        return self.Rack_Name

class Zone(models.Model):
    Zone_Name = models.CharField(max_length=50)
    idc = models.ForeignKey(IDC)
    def __unicode__(self):
        return self.Zone_Name
    def natural_key(self):
        return self.Zone_Name

class IP(models.Model):
    IP = models.IPAddressField()
    IP_Type = models.IntegerField()
    Device_id = models.IntegerField()
    def __unicode__(self):
        return self.IP

class MAC(models.Model):
    MAC = models.CharField(max_length=50)
    MAC_Type = models.IntegerField()
    Device_id = models.IntegerField()
    def __unicode__(self):
        return self.MAC

class Department(models.Model):
    Department_Name = models.CharField(max_length=50)
    Department_Contact = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Department_Name
    def natural_key(self):
        return self.Department_Name
   
class HostPhysical(models.Model):
    SN = models.CharField(max_length=30)
    Asset_SN = models.CharField(max_length=30)
    vendor = models.ForeignKey(Vendor,blank=True,null=True)
    model = models.ForeignKey(Model,blank=True,null=True)
    os = models.ForeignKey(OS,blank=True,null=True)
    kernel = models.ForeignKey(Kernel,blank=True,null=True)
    HostName = models.CharField(max_length=30)
    service = models.ForeignKey(Service,blank=True,null=True)
    department = models.ForeignKey(Department,blank=True,null=True)
    User = models.CharField(blank=True,null=True,max_length=30)
    UseInfo = models.CharField(blank=True,null=True,max_length=100)
    idc = models.ForeignKey(IDC,blank=True,null=True)
    zone = models.ForeignKey(Zone,blank=True,null=True)
    rack = models.ForeignKey(Rack,blank=True,null=True)
    Rack_Position = models.CharField(blank=True,null=True,max_length=20)
    cpu = models.ForeignKey(CPU,blank=True,null=True)
    CPU_Number = models.IntegerField(blank=True,null=True)
    memory = models.ForeignKey(Memory,blank=True,null=True)
    Memory_Number = models.IntegerField(blank=True,null=True)
    Memory_Size = models.CharField(max_length=20,blank=True,null=True) 
    disk = models.ForeignKey(Disk,null=True)
    Disk_Solt_Number = models.IntegerField(blank=True,null=True)
    Disk_Number = models.CharField(max_length=20,blank=True,null=True)
    Disk_Size = models.CharField(max_length=20,blank=True,null=True) 
    hba = models.ForeignKey(HBA,blank=True,null=True)
    HBA_Number = models.IntegerField(blank=True,null=True)
    pcie = models.ForeignKey(PCIE,blank=True,null=True)
    PCIE_Number = models.IntegerField(blank=True,null=True)
    nic = models.ForeignKey(NIC,blank=True,null=True)
    NIC_Number = models.IntegerField(blank=True,null=True)
    raid = models.ForeignKey(RAID,blank=True,null=True)
    RAID_Battery = models.CharField(max_length=30,null=True)
    RAID_Level = models.CharField(max_length=30,null=True)
    Manage_IP = models.IPAddressField(blank=True,null=True)
    LAN_IP = models.IPAddressField(blank=True,null=True)
    WAN_IP = models.IPAddressField(blank=True,null=True)
    RAC_IP = models.IPAddressField(blank=True,null=True)
    NAS_IP = models.IPAddressField(blank=True,null=True)
    VIP = models.IPAddressField(blank=True,null=True)
    WAN_mac = models.CharField(max_length=20,blank=True,null=True)
    LAN_mac = models.CharField(max_length=20,blank=True,null=True)
    RAC_mac = models.CharField(max_length=20,blank=True,null=True)
    Purchasing_Time = models.DateField(blank=True,null=True)
    Guarantee_Time = models.DateField(blank=True,null=True)
    Change_Time = models.DateField(blank=True,null=True)
    Change_Info = models.TextField(blank=True,null=True,max_length=100)
    Up_Time = models.DateField(blank=True,null=True)
    Status = models.IntegerField(blank=True,null=True)
    Remarks =  models.TextField(blank=True,null=True,max_length=100)
    def __unicode__(self):
        return self.Manage_IP


class HostVirtual(models.Model):
    os = models.ForeignKey(OS,blank=True,null=True)
    kernel = models.ForeignKey(Kernel,blank=True,null=True)
    HostName = models.CharField(max_length=30)
    service = models.ForeignKey(Service,blank=True,null=True)
    User = models.CharField(blank=True,null=True,max_length=30)
    department = models.ForeignKey(Department,blank=True,null=True)
    vCPU_Number = models.IntegerField(blank=True,null=True)
    Memory_Size = models.CharField(max_length=20,blank=True,null=True)
    Disk_Size = models.CharField(max_length=20,blank=True,null=True)
    Manage_IP = models.IPAddressField(blank=True,null=True)
    NAS_IP = models.IPAddressField(blank=True,null=True)
    VIP = models.IPAddressField(blank=True,null=True)
    SSH_Port = models.IntegerField(blank=True,null=True)
    LAN_IP = models.IPAddressField(blank=True,null=True)
    WAN_IP = models.IPAddressField(blank=True,null=True)
    Physical_Host_IP = models.IPAddressField(blank=True,null=True)
    WAN_mac = models.CharField(max_length=20,blank=True,null=True)
    LAN_mac = models.CharField(max_length=20,blank=True,null=True)
    RAC_mac = models.CharField(max_length=20,blank=True,null=True)
    Application_Time = models.DateField(blank=True,null=True) 
    Change_Time = models.DateField(blank=True,null=True)
    Change_Info = models.CharField(blank=True,null=True,max_length=100)
    Use_Info = models.CharField(blank=True,null=True,max_length=100)
    Use_Period = models.CharField(blank=True,null=True,max_length=100)
    Deploy_Path = models.CharField(blank=True,null=True,max_length=120)
    Up_Time = models.DateField(blank=True,null=True)
    Status = models.IntegerField(blank=True,null=True)
    Remarks =  models.CharField(blank=True,null=True,max_length=100)
    def __unicode__(self):
        return self.Manage_IP


class Loginlog(models.Model):
    action_time = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=30)
    action = models.IntegerField()
    result = models.IntegerField()
    message = models.CharField(blank=True,null=True,max_length=100)


class Accessories_Memory(models.Model):
    SN = models.CharField(max_length=30)
    Memory_Type = models.ForeignKey(Memory) 
    Status = models.IntegerField(blank=True,null=True)
    #Host_IP =  models.IPAddressField(blank=True,null=True)
    Host_SN = models.CharField(max_length=30)
class Accessories_Disk(models.Model):
    SN = models.CharField(max_length=30)
    Disk_Type = models.ForeignKey(Disk) 
    Status = models.IntegerField(blank=True,null=True)
    #Host_IP =  models.IPAddressField(blank=True,null=True)
    Host_SN = models.CharField(max_length=30)


class Application(models.Model):
    service =  models.CharField(max_length=100)
    service_level =  models.CharField(max_length=100)
    auto_deploy  =  models.CharField(max_length=100,blank=True,null=True)
    w_domain  =  models.CharField(max_length=200,blank=True,null=True)
    l_domain  =  models.CharField(max_length=200,blank=True,null=True)
    l_dns  =  models.CharField(max_length=100,blank=True,null=True)
    app_user  =  models.CharField(max_length=100,blank=True,null=True)
    hostname  =  models.CharField(max_length=200,blank=True,null=True)
    proxy =  models.CharField(max_length=100,blank=True,null=True)
    nginx =  models.CharField(max_length=100,blank=True,null=True)
    lan_ip =  models.CharField(max_length=200,blank=True,null=True)
    nas_ip =  models.CharField(max_length=100,blank=True,null=True)
    keepalived_ip =  models.CharField(max_length=100,blank=True,null=True)
    exec_user =  models.CharField(max_length=100,blank=True,null=True)
    app_path_port = models.CharField(max_length=1000,blank=True,null=True)
    config_file = models.CharField(max_length=1000,blank=True,null=True)
    firewall_port = models.CharField(max_length=100,blank=True,null=True)
    cash = models.CharField(max_length=100,blank=True,null=True)
    user_num = models.CharField(max_length=100,blank=True,null=True)
    key_app_related = models.CharField(max_length=100,blank=True,null=True)
    internet_app = models.CharField(max_length=100,blank=True,null=True)
    job_name = models.CharField(max_length=100,blank=True,null=True)
    svn_url = models.CharField(max_length=100,blank=True,null=True)
    scm_mark = models.CharField(max_length=100,blank=True,null=True)
    backup_mark = models.CharField(max_length=100,blank=True,null=True)
    
    
    


