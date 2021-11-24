from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
    )

    ordering = ('author',)