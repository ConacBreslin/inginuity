from django.contrib import admin
from .models import Gin, Distillery


class DistilleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'county',
        'province',
        'image',
        'website',
    )

    ordering = ('county',)


class GinAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'rating',
        'distillery',
    )

    ordering = ('price',)


# Register your models here.

admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Gin, GinAdmin)
