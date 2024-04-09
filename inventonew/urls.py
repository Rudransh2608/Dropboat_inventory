"""
URL configuration for inventonew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventonew import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('login/',auth_views.LoginView.as_view(template_name='login.html')),
    path('register_user/', views.register),
    path('logout/',views.logout_user),
    path('projects/',views.project),
    path('delete/<int:id>',views.deleteproject),
    path('staff/',views.staffo),
    path('order/',views.staffo),
    path('staff_only/',views.orderon),
    path('profile_user/', views.profile),
    path('profile_update/', views.profile_update),
    path('orders/', views.orders),
    path('delete_order/<int:id>',views.deleteorder),
    path('products/',views.products),
    path('delete_product/<int:id>',views.deleteproduct),
    path('about_us/',views.about),
    path('help_center/',views.help),
    path('',views.home),
    path('orders/pdf/',views.render_pdf_view),
    path('projects/pdf/',views.render_pdf_view_project),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
