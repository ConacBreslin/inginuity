"""File to create context for shopping bag"""

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from gins.models import Gin


def shoppingbag_contents(request):
    """To add purchased gins to shopping bag and quantities"""
    shoppingbag_items = []
    total = 0
    product_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, quantity in shoppingbag.items():
        gin = get_object_or_404(Gin, pk=item_id)
        total += quantity * gin.price
        product_count += quantity
        shoppingbag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'gin': gin,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    grand_total = delivery + total

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
