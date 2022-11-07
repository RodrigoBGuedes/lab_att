from django.contrib import admin
from django.urls import path

from config.core.views import core_page

app_name = 'core'
urlpatterns = [
    path('', core_page, name='core_page'),
]
