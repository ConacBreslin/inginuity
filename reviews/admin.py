from django.contrib import admin
from .models import Review
from gins.models import Distillery



class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'distillery',
        'body',
        'first_created_on',
        'last_editted_on'
    )

admin.site.register(Review, ReviewAdmin)