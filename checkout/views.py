from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """The view to get the shopping bag and order form and render template"""
    shoppingbag = request.session.get('shoppingbag', {})
    if not shoppingbag:
        messages.error(request, "You have nothing in your bag yet.")
        return redirect(reverse('gins'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JlFP9Cuph1nnB7l56cvop0saTpsLw1lyipZ4nZwt7bBittYHDDvlfnVFiVRrjKcL8paXkkMe0nGRqRzrRL7Lnsr00PgXcGwkc',
         'client_secret': 'test client secret',
    }

    return render(request, template, context)