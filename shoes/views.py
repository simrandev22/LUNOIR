from django.shortcuts import render,get_object_or_404
from .models import Shoe
# Create your views here.

def shoes(request):
    women_shoes=Shoe.objects.filter(gender="women")
    men_shoes=Shoe.objects.filter(gender='men')

    context={'women_shoes':women_shoes,
             'men_shoes':men_shoes,} 

    return render(request,'shoes.html',context)
        

def shoes_detail(request,pk):
    shoe=get_object_or_404(Shoe,pk=pk)
    related_shoes=Shoe.objects.filter(category=shoe.category).exclude(pk=shoe.pk)[:4]

    return render(request,'shoes_detail.html',{"shoe":shoe,"related_shoes":related_shoes,})

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