from django.contrib.auth.models import AbstractUser
from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    mac_address = models.CharField(max_length=200, blank=True)
    os = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    power = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    ipmi_ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    ipmi_mac_address = models.CharField(max_length=200, blank=True)
    ipmi_user_name = models.CharField(max_length=200, blank=True)
    ipmi_password = models.CharField(max_length=200, blank=True)
    vnc_port = models.IntegerField("VNCポート番号", blank=True, null=True)
    password = models.CharField("管理ユーザパスワード", max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_power_status(self):
        from core.utils.executor import get_power_for_node
        get_power_for_node.delay(self.pk)
        return self.power


class VirtualMachine(models.Model):
    CPU_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    # MB
    MEMORY_CHOICES = (
        ('512', '512MB'),
        ('1024', '1GB'),
        ('2048', '2GB'),
        ('4096', '4GB'),
    )

    # GB
    DISK_CHOICES = (
        ('10', '10GB'),
        ('20', '20GB'),
        ('50', '50GB'),
        ('100', '100GB'),
    )

    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    mac_address = models.CharField(max_length=200, blank=True)
    os = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    power = models.CharField(max_length=200, blank=True)
    host_server = models.ForeignKey(Node, related_name='virtual_machines')
    password = models.CharField("管理ユーザパスワード", max_length=200, blank=True)
    allocate_cpu = models.CharField("割り当てCPUコア数", max_length=200, blank=True, choices=CPU_CHOICES)
    allocate_memory = models.CharField("割り当てメモリ容量", max_length=200, blank=True, choices=MEMORY_CHOICES)
    allocate_disk = models.CharField("割り当てディスク容量", max_length=200, blank=True, choices=DISK_CHOICES)
    vnc_port = models.IntegerField("VNCポート番号", blank=True, null=True)


class Container(models.Model):
    #CPU_CHOICES = (
    #    ('1', '1'),
    #    ('2', '2'),
    #    ('3', '3'),
    #    ('4', '4'),
    #)

    # MB
    #EMORY_CHOICES = (
    #    ('512', '512MB'),
    #    ('1024', '1GB'),
    #    ('2048', '2GB'),
    #    ('4096', '4GB'),
    #)

    # GB
    #DISK_CHOICES = (
    #    ('10', '10GB'),
    #    ('20', '20GB'),
    #    ('50', '50GB'),
    #    ('100', '100GB'),
    #)

    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    mac_address = models.CharField(max_length=200, blank=True)
    os = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    power = models.CharField(max_length=200, blank=True)
    docker_host = models.ForeignKey(Node, related_name='virtual_machines')
    password = models.CharField("管理ユーザパスワード", max_length=200, blank=True)
    #allocate_cpu = models.CharField("割り当てCPUコア数", max_length=200, blank=True, choices=CPU_CHOICES)
    #allocate_memory = models.CharField("割り当てメモリ容量", max_length=200, blank=True, choices=MEMORY_CHOICES)
    #allocate_disk = models.CharField("割り当てディスク容量", max_length=200, blank=True, choices=DISK_CHOICES)
    #vnc_port = models.IntegerField("VNCポート番号", blank=True, null=True)


class OS(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    architecture = models.CharField(max_length=200)
    save_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ssh_public_key = models.TextField(blank=True, null=True)


class Metrics(models.Model):
    metrics_type = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=20)
    node = models.ForeignKey(Node)
