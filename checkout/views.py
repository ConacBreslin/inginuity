from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from shoppingbag.contexts import shoppingbag_contents
from django.conf import settings

import stripe


def checkout(request):
    """The view to get the shopping bag and order form and render template"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    shoppingbag = request.session.get('shoppingbag', {})
    if not shoppingbag:
        messages.error(request, "You have nothing in your bag yet.")
        return redirect(reverse('gins'))

    current_shoppingbag = shoppingbag_contents(request)
    total = current_shoppingbag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)