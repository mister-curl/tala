from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField(protocol='IPv4')
    ipmi_ip_address = models.GenericIPAddressField(protocol='IPv4')
    ipmi_user_name = models.CharField(max_length=200)
    ipmi_password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OS(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    architecture = models.CharField(max_length=200)
    save_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
