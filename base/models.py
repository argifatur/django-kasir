from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
# class Kategori(models.Model):
#     nama_kategori = models.CharField(max_length=200)

#     def __str__(self):
#         return self.nama_kategori

class Produk(models.Model):
    nama_produk 	= models.CharField(max_length=255)
    harga 	        = models.CharField(max_length=255, null=True)
    stok 		    = models.IntegerField(default=0, null=True)
    deskripsi 		= models.TextField()
    kategori 	    = models.CharField(max_length=255)
    author          = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created 	    = models.DateTimeField(auto_now_add=True)
    updated 	    = models.DateTimeField(auto_now=True)
    slug 		    = models.SlugField(blank=True, editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.nama_produk)
        super().save()

    def get_absolute_url(self):
        url_slug = {'slug':self.slug}
        return reverse('blog', kwargs = url_slug)
        
    def __str__(self):
        return self.nama_produk