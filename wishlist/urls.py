from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<int:product_id>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('add-shoe/<int:shoe_id>',views.add_shoe_to_wishlist,name='add_shoe_to_wishlist'),
    path('remove/<str:wishlist_id>/',views.remove_from_wishlist,name='remove_from_wishlist'),
]