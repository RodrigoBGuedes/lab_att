from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import Material, Box, Appointment


# Register your models here.

@admin.register(Material)
class Material(OrderedModelAdmin):
    list_display = ('code_material', 'description')


@admin.register(Box)
class Box(OrderedModelAdmin):
    list_display = ('code_box', 'description', 'is_empty')


@admin.register(Appointment)
class Appointment(OrderedModelAdmin):
    list_display = ('box', 'material', 'creator', 'created')

    readonly_fields = ('creator', 'created')

    fieldsets = (
        (None, {
            'fields': ('box', 'material')
        }),
        ('Log', {
            'classes': ('collapse',),
            'fields': ('creator', 'created')
        })

    )
