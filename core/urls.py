from django.urls import path
from .views import blog, home, add_vehiculo, edit_vehiculo, delete_vehiculo, momo

urlpatterns = [
    path('', home, name="home"),
    path('', momo, name="editaaar"),
    path('agregar-vehiculo/', add_vehiculo, name="add-vehiculo" ),
    path('editar-vehiculo/<pk>/', edit_vehiculo, name="edit-vehiculo" ),
    path('eliminar-vehiculo/<pk>/', delete_vehiculo, name="delete-vehiculo" ),
    path('casa_volver/', home, name="volver" ),
    path('blog/', blog, name="blog"),
]