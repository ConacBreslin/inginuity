from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Gin, Distillery
from .forms import GinForm


def all_gins(request):
    """The view to show all the gins, including sorting and search queries """

    gins = Gin.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                gins = gins.annotate(lower_name=Lower('name'))
            if sortkey == 'distillery':
                sortkey = 'distillery__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            gins = gins.order_by(sortkey)

            """I haven't used the category filtering used in Boutique ADO""" 

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('gins'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gins = gins.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'gins': gins,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'gins/gins.html', context)


def individual_gin(request, gin_id):
    """The view to show individual gins """

    gin = get_object_or_404(Gin, pk=gin_id)

    context = {
        'gin': gin,
    }

    return render(request, 'gins/individual_gin.html', context)


@login_required
def add_gin(request):
    """The view to add a gin to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, approved users can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GinForm(request.POST, request.FILES)
        if form.is_valid():
            gin= form.save()
            messages.success(request, 'You added a new gin!')
            return redirect(reverse('add_gin'))
        else:
            messages.error(request, 'This gin failed to add. Please check the form is valid.')
    else:
        form = GinForm()
        
    template = 'gins/add_gin.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_gin(request, gin_id):
    """The view to edit a gin on the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    gin = get_object_or_404(Gin, pk=gin_id)
    if request.method == 'POST':
        form = GinForm(request.POST, request.FILES, instance=gin)
        if form.is_valid():
            form.save()
            messages.success(request, 'You updated this gin!')
            return redirect(reverse('individual_gin', args=[gin.id]))
        else:
            messages.error(request, 'This gin failed to update. Please ensure the form is valid.')
    else:
        form = GinForm(instance=gin)
        messages.info(request, f'You are editing {gin.name}')

    template = 'gins/edit_gin.html'
    context = {
        'form': form,
        'gin': gin,
    }

    return render(request, template, context)


@login_required
def delete_gin(request, gin_id):
    """The view to delete a gin from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    gin = get_object_or_404(Gin, pk=gin_id)
    gin.delete()
    messages.success(request, 'That gin has been deleted!')
    return redirect(reverse('gins'))
