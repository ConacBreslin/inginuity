"""The view to render the home page"""

from django.shortcuts import render


def index(request):
    """The view to render the index page """

    return render(request, 'home/index.html')
