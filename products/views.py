from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Colour, Category, Style, Material, Backing, Manufacturer
from .forms import ProductForm 

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
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

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

    current_sorting = f'(sort)_(direction)'

    context = {
        'products': products,
        'search_term' : query,
        'current_categories': categories,
        'current_sorting': current_sorting,        
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


def add_product(request):
    """ Add Prooduct to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure you have correctly filled out form details.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)