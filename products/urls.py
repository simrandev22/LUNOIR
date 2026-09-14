from django.urls import path
from . import views

app_name="products"

urlpatterns = [
    path('',views.products,name='products'),
    path('search/',views.search,name="search"),
    path('<int:pk>/',views.productsdetail,name="productsdetail"),

]
