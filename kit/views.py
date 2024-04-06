from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
    """ 
    A view to show all products page
    """

    products = Product.objects.all()

    context = {
        "products" : products,
    }
    return render(request, 'kit/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show individual product detail page
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product" : product,
    }
    return render(request, 'kit/product_detail.html', context)