from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def index(request):
    featured_products = Product.objects.all()[:4]  # Show only 4 featured products
    return render(request, 'store/index.html', {'featured_products': featured_products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store/views.html", {"product": product})
