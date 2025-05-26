from django.db import models
from django.contrib.auth.models import User

class NetworkDevice(models.Model):
    building = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=100, blank=True, null=True)
    room_number = models.CharField(max_length=100, blank=True, null=True)
    local_ip = models.GenericIPAddressField(blank=True, null=True)
    public_ip = models.GenericIPAddressField(blank=True, null=True)
    remote_ip = models.GenericIPAddressField(blank=True, null=True)
    vlan = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    last_updated = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.building or ''} - {self.local_ip or ''}"