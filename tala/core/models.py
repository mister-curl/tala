from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    mac_address = models.CharField(max_length=200, blank=True)
    os = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    ipmi_ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    ipmi_mac_address = models.CharField(max_length=200, blank=True)
    ipmi_user_name = models.CharField(max_length=200, blank=True)
    ipmi_password = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class VirtualMachines(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)
    mac_address = models.CharField(max_length=200, blank=True)
    os = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, blank=True)
    host_server = models.ForeignKey(Node)


class OS(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    architecture = models.CharField(max_length=200)
    save_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
