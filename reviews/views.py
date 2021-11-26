from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from gins.models import Distillery
from.models import Review


def all_reviews(request):
    """The view to show all reviews on the site"""

    reviews = Review.objects.all()
    thisquery = None
    distilleries = Distillery.objects.all()

    if request.GET:
        if 'qq' in request.GET:
            thisquery = request.GET['qq']
            if not thisquery:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('reviews'))
            
            thequeries = Q(distillery__icontains=thisquery) | Q(body__icontains=thisquery)
            reviews = reviews.filter(thequeries)

    context = {
        'reviews': reviews,
        'search_term': thisquery,
    }

    return render(request, 'reviews/reviews.html', context)
