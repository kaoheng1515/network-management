from django.contrib import admin
from .models import NetworkDevice

@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ['building', 'floor', 'room_number', 'local_ip', 'public_ip', 'remote_ip', 'vlan', 'username', 'password', 'link', 'note']  # Updated
    search_fields = ['building', 'floor', 'room_number', 'local_ip', 'public_ip', 'remote_ip', 'vlan', 'username', 'link', 'note']  # Updated
    list_filter = ['building', 'floor', 'vlan']