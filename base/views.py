import http
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from .models import *
from django.http import HttpResponse
from . import forms
from datetime import datetime    

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def produkIndex(request):
    produks = Produk.objects.all()
    context = {'produks':produks}
    return render(request,'operator/produk/index.html', context)

def produkTambah(request):
    form = forms.ProdukForm()
    if request.method == 'POST':
        Produk.objects.create(
            nama_produk=request.POST.get('nama_produk'),
            deskripsi=request.POST.get('deskripsi'),
            kategori=request.POST.get('kategori'),
            harga=request.POST.get('harga'),
            stok=request.POST.get('stok'),
            author=request.user,
        )
        messages.success(request, "Sukses Menambah Produk." )
        return redirect('produk')
    context = {'form':form}
    return render(request,'operator/produk/tambah.html', context)

def produkHapus(request,pk):
    produk = Produk.objects.get(id=pk)
    if request.method == 'POST':
        produk.delete()
        messages.success(request, "Sukses Menghapus produk." )
        return redirect('produk')
    else:
        messages.error(request, 'Terdapat Error Saat Hapus produk. Pastikan Data Yang Ingin Dihapus Tidak Terkait Dengan Data Lain!', extra_tags="danger")
    return render(request, 'operator/produk/hapus.html', {'obj':produk})

def produkEdit(request,pk):
    produk = Produk.objects.get(id=pk)
    form = forms.ProdukForm(instance=produk)
    if request.method == 'POST':
        form = forms.ProdukForm(request.POST, instance=produk)
        produk.nama_produk  = request.POST.get('nama_produk')
        produk.deskripsi  = request.POST.get('deskripsi')
        produk.harga  = request.POST.get('harga')
        produk.kategori  = request.POST.get('kategori')
        produk.stok  = request.POST.get('stok')
        produk.save()
        messages.success(request, "Sukses Mengubah Produk." )
        return redirect('produk')

    context = {'form':form,'produk':produk}
    return render(request, 'operator/produk/edit.html', context)

def produkDetail(request,pk):
    produk = Produk.objects.get(id=pk)
    context = {'produk':produk}
    return render(request, 'operator/produk/detail.html', context)

def dashboard(request):
    return render(request,'operator/dashboard.html')