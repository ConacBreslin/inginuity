from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from gins.models import Gin, Distillery



def wholesite_search(request):
    distilleries = Distillery.objects.all()
    gins = Gin.objects.all()

    context = {
            'distilleries': distilleries,
            'gins': gins,
        }

    return render(request, 'wholesitesearch/wholesitesearch.html', context)


