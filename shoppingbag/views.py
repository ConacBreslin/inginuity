from django.shortcuts import render

# Create your views here.


def view_shoppingbag(request):
    """ The view to renders the bag contents page """

    return render(request, 'shoppingbag/shoppingbag.html')