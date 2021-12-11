from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from gins.models import Gin, Distillery
from reviews.models import Review


def wholesite_search(request):
    q = request.GET.get('q')
    if not q:
        messages.error(request, "You didn't enter any search criteria!")
        return redirect(reverse('home'))
    distilleries = Distillery.objects.filter(Q(name__icontains=q) |
                                             Q(description__icontains=q) |
                                             Q(county__icontains=q) |
                                             Q(province__icontains=q))
    gins = Gin.objects.filter(Q(name__icontains=q) |
                              Q(description__icontains=q))
    reviews = Review.objects.filter(Q(body__icontains=q) |
                                    Q(username__username__icontains=q) |
                                    Q(title__icontains=q))

    context = {
            'distilleries': distilleries,
            'gins': gins,
            'reviews': reviews,
            'q': q
        }

    return render(request, 'wholesitesearch/wholesitesearch.html', context)
