from django.forms import ModelForm
from .models import *


class ProdukForm(ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'
