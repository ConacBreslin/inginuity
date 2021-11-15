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
    }

    return render(request, template, context)