from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gins.models import Distillery
from .models import Review


def all_reviews(request):
    """The view to show all reviews"""

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)


@login_required
def add_review(request):
    """The view to add a review to the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'You added a new review!')
            return redirect(
                reverse('reviews')
                )
        else:
            messages.error(
                request, 'This review failed to add. ' +
                'Please check the form is valid.'
                )
    else:
        form = ReviewForm()

    template = 'reviews/reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """The view to edit a review"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'You updated this rev!')
            return redirect(
                reverse('reviews')
                )
        else:
            messages.error(
                request, 'This review failed to update. ' +
                'Please ensure the form is valid.'
                )
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing a review of {distillery.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """The view to delete a review from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'That review has been deleted!')
    return redirect(reverse('reviews'))

