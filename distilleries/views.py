from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from gins.models import Distillery



def all_distilleries(request):
    """The view to show all distilleries, including sorting and search queries """

    distilleries = Distillery.objects.all()

    context = {
        'distilleries': distilleries,
    }

    return render(request, 'distilleries/distilleries.html', context)


def individual_distillery(request, distillery_id):
    """The view to show individual distilleries"""

    distillery = get_object_or_404(Distillery, pk=distillery_id)

    context = {
        'distillery': distillery,
    }

    return render(request, 'distilleries/individual_distillery.html', context)


   