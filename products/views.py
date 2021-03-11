from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """A view that shows all products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

<<<<<<< HEAD
    return render(request, 'products/product_detail.html', context)
=======
    return render(request, 'products/product_detail.html', context)

>>>>>>> fe5eecf668782daa0272b2d977ef857dcd7fea50
