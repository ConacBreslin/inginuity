from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from gins.models import Distillery
from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    """The view to show all reviews including sorting"""

    reviews = Review.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # if sortkey == 'author':
            #     sortkey = 'lower_author'
            reviews = reviews.order_by(sortkey)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            reviews = reviews.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'
    
    
    context = {
        'reviews': reviews,
        'current_sorting': current_sorting,              
            }


    return render(request, 'reviews/reviews.html', context)



def add_review(request):
    """ Add a review to a distillery """
    form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)