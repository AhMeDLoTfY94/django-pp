from django.shortcuts import render
from .models import Product


def product(request):

          return render(request,'products/product.html')

def products(request):
          obj=Product.objects.all()
          context={
                    'obj':obj
          }

          return render(request,'products/products.html',context)

