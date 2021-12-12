"""The view to render the home page"""

from django.shortcuts import render


def index(request):
    """The view to render the index page """

    return render(request, 'home/index.html')


def geninfo(request):
    """The view to render the geninfo page """

    return render(request, 'home/geninfo.html')
