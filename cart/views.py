from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from shoes.models import Shoe


# =========================================================
# CART PAGE
# =========================================================

def cart(request):

    cart_items = request.session.get("cart", {})

    products = []

    for item_id, quantity in cart_items.items():

        # =================================================
        # SHOE
        # =================================================

        if item_id.startswith("shoe_"):

            shoe_id = item_id.replace("shoe_", "")

            try:
                shoe = Shoe.objects.get(id=shoe_id)

            except Shoe.DoesNotExist:
                continue

            products.append({
                "product": shoe,
                "quantity": quantity,
                "total": shoe.price * quantity,
                "type": "shoe",
                "id": shoe.id,
                "cart_id": item_id,
            })

        # =================================================
        # NORMAL PRODUCT
        # =================================================

        else:

            try:
                product = Product.objects.get(id=item_id)

            except Product.DoesNotExist:
                continue

            products.append({
                "product": product,
                "quantity": quantity,
                "total": product.price * quantity,
                "type": "product",
                "id": product.id,
                "cart_id": item_id,
            })

    # =====================================================
    # CART TOTAL
    # =====================================================

    cart_total = sum(item["total"] for item in products)

    return render(
        request,
        "cart.html",
        {
            "cart_items": products,
            "cart_total": cart_total,
        }
    )


# =========================================================
# ADD NORMAL PRODUCT TO CART
# =========================================================

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    else:
        cart[product_id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart:cart")


# =========================================================
# ADD SHOE TO CART
# =========================================================

def add_shoe_to_cart(request, shoe_id):

    shoe = get_object_or_404(Shoe, id=shoe_id)

    cart = request.session.get("cart", {})

    cart_id = f"shoe_{shoe_id}"

    if cart_id in cart:
        cart[cart_id] += 1

    else:
        cart[cart_id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart:cart")


# =========================================================
# INCREASE QUANTITY
# =========================================================

def increase_quantity(request, cart_id):

    cart = request.session.get("cart", {})

    cart_id = str(cart_id)

    if cart_id in cart:
        cart[cart_id] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart:cart")


# =========================================================
# DECREASE QUANTITY
# =========================================================

def decrease_quantity(request, cart_id):

    cart = request.session.get("cart", {})

    cart_id = str(cart_id)

    if cart_id in cart:

        cart[cart_id] -= 1

        if cart[cart_id] <= 0:
            del cart[cart_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart:cart")


# =========================================================
# REMOVE FROM CART
# =========================================================

def remove_from_cart(request, cart_id):

    cart = request.session.get("cart", {})

    cart_id = str(cart_id)

    if cart_id in cart:
        del cart[cart_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart:cart")