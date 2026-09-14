from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def cart(request):
    cart_items = request.session.get("cart", {})

    products = []

    for product_id, quantity in cart_items.items():
        product = get_object_or_404(Product, id=product_id)

        products.append({
            "product": product,
            "quantity": quantity,
            "total": product.price * quantity,
        })

    cart_total = sum(item["total"] for item in products)

    return render(request, "cart.html", {
        "cart_items": products,
        "cart_total": cart_total,
    })


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