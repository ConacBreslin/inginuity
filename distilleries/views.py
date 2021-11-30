from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from gins.models import Gin, Distillery
from .forms import DistilleryForm


def all_distilleries(request):
    """The view to show all distilleries"""

    distilleries = Distillery.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                distilleries = distilleries.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            distilleries = distilleries.order_by(sortkey)   

    current_sorting = f'{sort}_{direction}'
    context = {
        'distilleries': distilleries,
        'current_sorting': current_sorting,
    }

    return render(request, 'distilleries/distilleries.html', context)


def individual_distillery(request, distillery_id):
    """The view to show individual distilleries"""

    distillery = get_object_or_404(Distillery, pk=distillery_id)

    context = {
        'distillery': distillery,
    }

    return render(request, 'distilleries/individual_distillery.html', context)


@login_required
def add_distillery(request):
    """The view to add a distillery to the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DistilleryForm(request.POST, request.FILES)
        if form.is_valid():
            distillery = form.save()
            messages.success(request, 'You added a new distillery!')
            return redirect(reverse('individual_distillery', args=[distillery.id]))
        else:
            messages.error(request, 'This distillery failed to add. Please check the form is valid.')
    else:
        form = DistilleryForm()
        
    template = 'distilleries/add_distillery.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_distillery(request, distillery_id):
    """The view to edit a distillery"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    distillery = get_object_or_404(Distillery, pk=distillery_id)
    if request.method == 'POST':
        form = DistilleryForm(request.POST, request.FILES, instance=distillery)
        if form.is_valid():
            form.save()
            messages.success(request, 'You updated this distillery!')
            return redirect(reverse('individual_distillery', args=[distillery.id]))
        else:
            messages.error(request, 'This distillery failed to update. Please ensure the form is valid.')
    else:
        form = DistilleryForm(instance=distillery_id)
        messages.info(request, f'You are editing {distillery.name}')

    template = 'distilleries/edit_distillery.html'
    context = {
        'form': form,
        'distillery': distillery,
    }

    return render(request, template, context)



@login_required
def delete_distillery(request, distillery_id):
    """The view to delete a distillery from the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only approved users can do this.')
        return redirect(reverse('home'))

    distillery = get_object_or_404(Distillery, pk=distillery_id)
    distillery.delete()
    messages.success(request, 'That distillery has been deleted!')
    return redirect(reverse('distilleries'))