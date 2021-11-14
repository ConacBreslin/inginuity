from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_shoppingbag(request):
    """ The view to renders the bag contents page """

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, item_id):
    """The view to add quatity of items to shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingbag = request.session.get('shoppingbag', {})

    if item_id in list(shoppingbag.keys()):
        shoppingbag[item_id] += quantity
    else:
        shoppingbag[item_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def adjust_shoppingbag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    shoppingbag = request.session.get('shoppingbag', {})
    
    if quantity > 0:
        shoppingbag[item_id] = quantity
    else:
        shoppingbag.pop(item_id)

    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))


def remove_from_shoppingbag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        shoppingbag = request.session.get('shoppingbag', {})
            
        shoppingbag.pop(item_id)

        request.session['shoppingbag'] = shoppingbag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)