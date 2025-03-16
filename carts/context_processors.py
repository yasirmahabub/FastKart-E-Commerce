﻿from django.db.models import Sum

from .models import Cart, CartItem
from .utils import get_session_key


def counter(request):
    if "admin" in request.path:
        return {}

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).last()
    else:
        cart = Cart.objects.filter(session_key=get_session_key(request)).last()

    if cart:
        cart_count = (
            CartItem.objects.filter(cart=cart).aggregate(
                total_quantity=Sum("quantity")
            )["total_quantity"]
            or 0
        )
    else:
        cart_count = 0

    return {"cart_count": cart_count}
