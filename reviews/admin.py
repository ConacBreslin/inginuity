from django.contrib import admin
from .models import Review
from gins.models import Distillery
from django.contrib.auth.models import User

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'body',
        'first_created_on',
        'last_editted_on',
    )

admin.site.register(Review, ReviewAdmin)

