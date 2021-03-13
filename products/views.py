from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Colour, Category, Style, Material, Backing, Manufacturer

# Create your views here.


def all_products(request):
    """A view that shows all products"""

    products = Product.objects.all()
    query = None
    categories = None
    styles = None
    material = None
    backing = None
    manufacturer = None

    if request.GET:
        if 'style' in request.GET:
            styles = request.GET['style'].split(',')
            products = products.filter(style__name__in=styles)
            styles = Style.objects.filter(name__in=styles)

        if 'material' in request.GET:
            materials = request.GET['material'].split(',')
            products = products.filter(material__name__in=materials)
            materials = Material.objects.filter(name__in=materials)

        if 'backing' in request.GET:
            backings = request.GET['backing'].split(',')
            products = products.filter(backing__name__in=backings)
            backings = Backing.objects.filter(name__in=backings)

        if 'manufacturer' in request.GET:
            manufacturers = request.GET['manufacturer'].split(',')
            products = products.filter(manufacturer__name__in=manufacturers)
            manufacturers = Manufacturer.objects.filter(name__in=manufacturers)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term' : query,
        'current_categories': categories,
        'current_styles': styles,
        
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    colours = Colour.objects.all()

    context = {
        'product': product,
        'colours': colours,
    }

    return render(request, 'products/product_detail.html', context)
