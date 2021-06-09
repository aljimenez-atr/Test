from django.urls import path
from .views import blog, home, add_vehiculo, edit_vehiculo, delete_vehiculo, momo

urlpatterns = [
    path('', home, name="home"),

]