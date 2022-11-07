"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from config.core.views import appointment_scan, appointment_voice, page_logout, core_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core_page', core_page, name='core_page'),
    path('', include('config.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('appointment_scan', appointment_scan, name='appointment_scan'),
    path('appointment_voice', appointment_voice, name='appointment_voice'),
    path('logout', page_logout, name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
]
