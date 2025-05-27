from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import NetworkDevice
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import urlencode
from django.urls import reverse

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Handle search query
    search_query = request.GET.get('search', '')
    devices = NetworkDevice.objects.all()
    
    if search_query:
        devices = devices.filter(
            Q(building__icontains=search_query) |
            Q(floor__icontains=search_query) |
            Q(room_number__icontains=search_query) |
            Q(local_ip__icontains=search_query) |
            Q(public_ip__icontains=search_query) |
            Q(remote_ip__icontains=search_query) |
            Q(vlan__icontains=search_query) |
            Q(username__icontains=search_query) |
            Q(link__icontains=search_query)
        )

    # Add pagination
    paginator = Paginator(devices, 10)
    page = request.GET.get('page')
    try:
        devices_paginated = paginator.page(page)
    except PageNotAnInteger:
        devices_paginated = paginator.page(1)
    except EmptyPage:
        devices_paginated = paginator.page(paginator.num_pages)

    new_device_id = None

    if request.method == 'POST':
        if 'add' in request.POST:
            building = request.POST.get('building', None)
            floor = request.POST.get('floor', None)
            room_number = request.POST.get('room_number', None)
            local_ip = request.POST.get('local_ip', None) or "0.0.0.0"
            public_ip = request.POST.get('public_ip', None) or "0.0.0.0"
            remote_ip = request.POST.get('remote_ip', None) or "0.0.0.0"
            vlan = request.POST.get('vlan', None)
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)  # Let the model handle the default
            link = request.POST.get('link', None)

            new_device = NetworkDevice.objects.create(
                building=building,
                floor=floor,
                room_number=room_number,
                local_ip=local_ip,
                public_ip=public_ip,
                remote_ip=remote_ip,
                vlan=vlan,
                username=username,
                password=password,  # Will use model default if None
                link=link,
            )
            messages.success(request, 'Device added successfully!')
            base_url = reverse('home')
            query_params = {'new_device_id': new_device.id}
            url = f'{base_url}?{urlencode(query_params)}'
            return redirect(url)
        elif 'update' in request.POST and 'device_id' in request.POST:
            device_id = request.POST.get('device_id')
            device = get_object_or_404(NetworkDevice, id=device_id)
            device.building = request.POST.get('building', device.building)
            device.floor = request.POST.get('floor', device.floor)
            device.room_number = request.POST.get('room_number', device.room_number)
            device.local_ip = request.POST.get('local_ip', device.local_ip) or "0.0.0.0"
            device.public_ip = request.POST.get('public_ip', device.public_ip) or "0.0.0.0"
            device.remote_ip = request.POST.get('remote_ip', device.remote_ip) or "0.0.0.0"
            device.vlan = request.POST.get('vlan', device.vlan)
            device.username = request.POST.get('username', device.username)
            device.password = request.POST.get('password', device.password)  # Let the model handle the default
            device.link = request.POST.get('link', device.link)
            device.save()
            messages.success(request, 'Device updated successfully!')
            return redirect('home')
        elif 'delete' in request.POST and 'device_id' in request.POST:
            device_id = request.POST.get('device_id')
            device = get_object_or_404(NetworkDevice, id=device_id)
            device.delete()
            messages.success(request, 'Device deleted successfully!')
            return redirect('home')

    new_device_id = request.GET.get('new_device_id')
    return render(request, 'network/home.html', {
        'devices': devices_paginated,
        'new_device_id': new_device_id,
        'search_query': search_query,
    })

def login_view(request):
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            return render(request, 'network/login.html', {'error': 'Invalid credentials', 'next': next_url})
    return render(request, 'network/login.html', {'next': next_url})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')