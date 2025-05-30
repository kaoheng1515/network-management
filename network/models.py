from django.db import models

class NetworkDevice(models.Model):
    building = models.CharField(max_length=100, default="Unknown", null=True, blank=True)
    floor = models.CharField(max_length=100, default="Unknown", null=True, blank=True)
    room_number = models.CharField(max_length=100, default="Unknown", null=True, blank=True)
    local_ip = models.GenericIPAddressField(default="0.0.0.0", null=True, blank=True)
    public_ip = models.GenericIPAddressField(default="0.0.0.0", null=True, blank=True)
    remote_ip = models.GenericIPAddressField(default="0.0.0.0", null=True, blank=True)
    vlan = models.CharField(max_length=50, default="Unknown", null=True, blank=True)
    username = models.CharField(max_length=100, default="Unknown", null=True, blank=True)
    password = models.CharField(max_length=100, default="MySecurePassword123!", null=True, blank=True)
    link = models.URLField(default="https://example.com", null=True, blank=True)
    note = models.TextField(default="No note", null=True, blank=True)  # Renamed from remark

    def __str__(self):
        return f"{self.building or 'Unknown'} - {self.room_number or 'Unknown'}"