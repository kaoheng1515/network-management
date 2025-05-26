from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewer_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('viewer/', views.viewer_view, name='network_home'),
    path('admin/', views.admin_view, name='admin_home'),
    path('admin/update/<int:device_id>/', views.update_device, name='update_device'),
    path('admin/delete/<int:device_id>/', views.delete_device, name='delete_device'),
]