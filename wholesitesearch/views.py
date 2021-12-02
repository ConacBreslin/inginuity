from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from gins.models import Gin, Distillery
from reviews.models import Review



def wholesite_search(request):
    q = request.GET.get('q')
    if not q:
        messages.error(request, "You didn't enter any search criteria!")
        return redirect(reverse('home'))
    distilleries = Distillery.objects.filter( Q(name__icontains=q) | Q(description__icontains=q)     | Q(county__icontains=q) | Q(province__icontains=q)) 
    gins = Gin.objects.filter( Q(name__icontains=q) | Q(description__icontains=q) )
    reviews = Review.objects.filter( Q(body__icontains=q) |  Q(username__username__icontains=q))

#Having difficulty getting username and distillery into this search - is it because they are both FKs?
#reviews = Review.objects.filter( Q ( body__icontains=q) | Q(review.user.username__icontains=q) | Q(review.distillery.name__icontains=q) )
    context = {
            'distilleries': distilleries,
            'gins': gins,
            'reviews': reviews,
        }

    return render(request, 'wholesitesearch/wholesitesearch.html', context)

