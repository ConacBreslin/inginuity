from django.shortcuts import render, get_object_or_404
from .models import Gin

# Create your views here.

def all_gins(request):
    """ A view to show all tyhe gins and sorting and search queries """

    gins = Gin.objects.all()

    context = {
        'gins': gins,
    }

    return render(request, 'gins/gins.html', context)


def individual_gin(request, gin_id):
    """ A view to show individual gin details """

    gin = get_object_or_404(Gin, pk=gin_id)

    context = {
        'gin': gin,
    }

    return render(request, 'gins/individual_gin.html', context)