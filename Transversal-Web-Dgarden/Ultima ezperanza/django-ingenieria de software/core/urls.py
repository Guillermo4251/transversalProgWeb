from operator import index
from turtle import home
from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [ 
     path('', Index, name="Index"),
     path('Regist', Regist, name="Regist"),
     path('CarritoCompras', CarritoCompras, name="CarritoCompras"),
     path('CarritoComprasHistorial', CarritoComprasHistorial, name="CarritoComprasHistorial"),
     path('IniciosesionAdmin', IniciosesionAdmin, name="IniciosesionAdmin"),
     path('crudproductos', crudproductos, name="crudproductos"),
     path('Formulario', Formulario, name="Formulario"),
     path('FormularioEmp', FormularioEmp, name="FormularioEmp"),
     path('IndexDescuento', IndexDescuento, name="IndexDescuento"),
     path('Suscribirse', Suscribirse, name="Suscribirse"),
     path('Pago', Pago, name="Pago"),
     path('crudproductos', crudproductos, name="crudproductos"),
     path('PagoSus', PagoSus, name="PagoSus"),
     path('crud2', crud2, name="crud2"),
     path('pagina', pagina, name="pagina"),    
     path('InicioSesion/', LoginView.as_view(template_name='core/InicioSesion.html'), name="InicioSesion"),
     path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
     path('crud', crud, name="crud"),
     path('modificarSuscriptor/<id>', modificarSuscriptor , name="modificarSuscriptor"),
     path('eliminarPromocion/<id>', eliminarPromocion , name="eliminarPromocion"),
     path('crear_promocion', crear_promocion , name="crear_promocion"),
     path('crud_productos', crud_productos, name="crud_productos"),
     path('modificar_Producto/<id>', modificar_Producto , name="modificar_Producto"),
     path('crear_producto', crear_producto , name="crear_producto"),
     path('eliminarProducto/<id>', eliminarProducto , name="eliminarProducto"),
     
     
]