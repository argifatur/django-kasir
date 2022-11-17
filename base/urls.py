from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('operator/dashboard', views.dashboard, name="dashboard"),
    path('operator/produk', views.produkIndex, name="produk"),
    path('operator/produk/tambah', views.produkTambah, name="produk-tambah"),
    path('operator/produk/hapus/<int:pk>', views.produkHapus, name="produk-hapus"),
    path('operator/produk/edit/<int:pk>', views.produkEdit, name="produk-edit"),
    path('operator/produk/detail/<int:pk>', views.produkDetail, name="produk-detail"),
]
