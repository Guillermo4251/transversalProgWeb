from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class promoform(ModelForm):
    class Meta:
        model = promocion
        fields = [ 'nombre', 'descuento', 'idProducto']


class promonew(ModelForm):
    class Meta:
        model = promocion
        fields = [  'idpromo','nombre', 'descuento', 'idProducto']


class productoform(ModelForm):
    class Meta:
        model = Producto
        fields = [ 'NombreProducto', 'Valor', 'stock']


class productonew(ModelForm):
    class Meta:
        model = Producto
        fields = [  'IdProducto','NombreProducto', 'Valor', 'stock']


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email","password1","password2"]
