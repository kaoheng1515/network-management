from django.contrib import admin
from .models import NetworkDevice

@admin.register(NetworkDevice)
class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ['building', 'floor', 'room_number', 'local_ip', 'public_ip', 'remote_ip', 'vlan', 'username', 'password', 'link', 'created_at']
    search_fields = ['building', 'floor', 'room_number', 'local_ip', 'public_ip', 'remote_ip', 'vlan', 'username', 'link']
    list_filter = ['building', 'floor', 'vlan']