from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from gins.models import Gin, Distillery


def wholesite_search(request):
    q = request.GET.get('q')
    distilleries = Distillery.objects.filter( Q(name__icontains=q) | Q(description__icontains=q) | Q(county__icontains=q))
    gins = Gin.objects.filter( Q(name__icontains=q) | Q(description__icontains=q) )
    print(distilleries)
    print(gins)
    context = {
            'distilleries': distilleries,
            'gins': gins,
        }

    return render(request, 'wholesitesearch/wholesitesearch.html', context)
