from django.shortcuts import get_object_or_404, render,redirect
from products.models import Product
from shoes.models import Shoe


def wishlist(request):
    wishlist_items=request.session.get('wishlist',{})

    items=[]

    for item_id in wishlist_items:

        if item_id.startswith("shoes_"):
            shoe_id=item_id.replace("shoe_","")

            try:
                shoe=Shoe.objects.get(id=shoe_id)
            except Shoe.DoesNotExist:
                continue
            items.append({
                "item":shoe,
                "type":"shoe",
                "id":shoe.id,
                "wishlist_id":item_id,
            })     

        else:

              try:
                product=Product.objects.get(id=item_id)
              except Product.DoesNotExist:

                continue

              items.append({'item':product,
                        'type':product,
                        'id':product.id,
                        'wishlist_id':item_id,})
    return render(request,'wishlist.html',{'wishlist_items':items,})

# =========================================================
# ADD / REMOVE CLOTHING FROM WISHLIST
# =========================================================

def add_to_wishlist(request,product_id):
    product=get_object_or_404(Product,id=product_id)

    wishlist=request.session.get('wishlist',{})

    product_id=str(product_id)

    if product_id in wishlist:
        del wishlist[product_id]
    else:
        wishlist[product_id]=1

    request.session['wishlist']=wishlist
    request.session.modified=True

    return redirect(request.META.get('HTTP_REFERER','wishlist')) 


  
# =========================================================
# ADD  SHOE FROM WISHLIST
# =========================================================

def add_shoe_to_wishlist(request, shoe_id):
    shoe=get_object_or_404(Shoe,id=shoe_id) 
    wishlist=request.session.get('wishlist',{})

    wishlist_id=f"shoe_{shoe_id}"

    if wishlist_id in wishlist:

        del wishlist[wishlist_id]
    else:
        wishlist[wishlist_id]=1

    request.session['wishlist']=wishlist
    request.session.modified=True

    return redirect(request.META.get("HTTP_REFERER","wishlist"))  

# =========================================================
# REMOVE ITEM FROM WISHLIST
# =========================================================

def remove_from_wishlist(request,wishlist_id):
    wishlist=request.session.get("wishlist",{})

    wishlist_id=str(wishlist_id)

    if wishlist_id in wishlist:
        del wishlist[wishlist_id]
    request.session['wishlist']=wishlist
    request.session.modified=True

    return redirect('wishlist')         
