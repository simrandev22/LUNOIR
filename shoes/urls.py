from django.urls import path
from .import views

app_name="shoes"

urlpatterns = [
    path("",views.shoes,name="shoes"),
    path("<int:pk>/",views.shoes_detail,name="shoes_detail")
]
