from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .models import NetworkDevice
from django.contrib.auth.models import Group

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_viewer(user):
    return user.groups.filter(name='Viewer').exists()

def login_view(request):
    next_url = request.GET.get('next', '/viewer/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url.startswith('/') and '://' not in next_url:  # Basic validation
                return redirect(next_url)
            return redirect('/viewer/')
        else:
            return render(request, 'network/login.html', {'error': 'Invalid credentials', 'next': next_url})
    return render(request, 'network/login.html', {'next': next_url})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(is_viewer)
def viewer_view(request):
    devices = NetworkDevice.objects.all()
    return render(request, 'network/viewer.html', {'devices': devices})

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    devices = NetworkDevice.objects.all()
    if request.method == 'POST' and 'add' in request.POST:
        building = request.POST.get('building')
        floor = request.POST.get('floor')
        room_number = request.POST.get('room_number')
        local_ip = request.POST.get('local_ip')
        public_ip = request.POST.get('public_ip')
        remote_ip = request.POST.get('remote_ip')
        vlan = request.POST.get('vlan')
        username = request.POST.get('username')
        password = request.POST.get('password')
        link = request.POST.get('link')

        NetworkDevice.objects.create(
            building=building, floor=floor, room_number=room_number,
            local_ip=local_ip, public_ip=public_ip, remote_ip=remote_ip,
            vlan=vlan, username=username, password=password, link=link,
            created_by=request.user
        )
        return redirect('admin_home')
    return render(request, 'network/admin.html', {'devices': devices})

@login_required
@user_passes_test(is_admin)
def update_device(request, device_id):
    device = get_object_or_404(NetworkDevice, id=device_id)
    if request.method == 'POST':
        device.building = request.POST.get('building')
        device.floor = request.POST.get('floor')
        device.room_number = request.POST.get('room_number')
        device.local_ip = request.POST.get('local_ip')
        device.public_ip = request.POST.get('public_ip')
        device.remote_ip = request.POST.get('remote_ip')
        device.vlan = request.POST.get('vlan')
        device.username = request.POST.get('username')
        device.password = request.POST.get('password')
        device.link = request.POST.get('link')
        device.save()
        return redirect('admin_home')
    return render(request, 'network/update.html', {'device': device})

@login_required
@user_passes_test(is_admin)
def delete_device(request, device_id):
    device = get_object_or_404(NetworkDevice, id=device_id)
    if request.method == 'POST':
        device.delete()
        return redirect('admin_home')
    return render(request, 'network/delete.html', {'device': device})