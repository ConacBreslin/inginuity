from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gins.models import Gin, Distillery



def reviews(request):
    """The view to show all distilleries"""

    

    return render(request, 'reviews/reviews.html', )