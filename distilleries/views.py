from django.shortcuts import render

from django.shortcuts import render
from gins.models import Distillery



def all_distilleries(request):
    """The view to show all distilleries, including sorting and search queries """

    distilleries = Distillery.objects.all()

    context = {
        'distilleries': distilleries,
    }

    return render(request, 'distilleries/distilleries.html', context)