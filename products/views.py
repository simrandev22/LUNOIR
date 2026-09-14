from django.shortcuts import render,get_object_or_404
from django.db.models import Q

from .models import Product

# Create your views here.
def products(request):
    products=Product.objects.all()

    selected_category=request.GET.get('category')

    if selected_category:
        products=products.filter(category__slug=selected_category)

        

    return render(request,'products.html',{'products':products,'selected_category':selected_category,})

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


def productsdetail(request,pk):
    product = get_object_or_404(Product,pk=pk)

    return render(request,'productsdetail.html',{'product':product,})