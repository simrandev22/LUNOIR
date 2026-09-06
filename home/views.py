from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.
def home(request):
    return render(request,'home.html')

def search(request):
    query=request.GET.get('q','').strip()
    results=Product.objects.none()

    if query:
        results=Product.objects.filter(
        Q(name__icontains=query)|
        Q(description__icontains=query)|
        Q(category__name__icontains=query)|
        Q(category__section__icontains=query)|
        Q(category__group__icontains=query)|
        Q(category__slug__icontains=query)
        ).distinct()


    return render(request,'search.html',{'query':query,'results':results})

def wishlist(request):
    return render(request,'wishlist.html')