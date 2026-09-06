from django.shortcuts import render,get_object_or_404
from django.db.models import Q

from .models import Product

# Create your views here.
def products(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})

def search(request):
    query=request.GET.get("q","").strip()
    results=Product.objects.none()

    if query:
        results=Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        ).distinct()

    context={
        "query":query,
        "results":results,
    }    

    return render(request,'search.html',context)

def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)

    related_products=Product.objects.exclude(pk=product.pk)[:5]

    return render(request,'product_detail.html',{'product':product,'related_products':related_products,})