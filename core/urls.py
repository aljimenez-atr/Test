from django.urls import path
from .views import menu,registro,login,logout
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',menu, name="menu"),    
    path('registro/',registro,name="registro"),
    path('login/',LoginView.as_view(template_name='core/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='core/logout.html'),name="logout")
    
]