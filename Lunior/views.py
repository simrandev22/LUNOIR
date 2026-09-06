from django.shortcuts import render


def home(request):
    return render(request,'home/home.html')

def accounts(request):
    return render(request,'accounts/accounts.html')

def products(request):
    return render(request,'products/products.html')