from django.urls import path
from .views import menu,registro,login


urlpatterns = [
    path('',menu, name="menu"),    
    path('registro/',registro,name="registro"),
    path('login/',login,name="login"),
    


]