from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_bag(request):
    """ View that returns bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of product to the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    carpet_width = 0
    carpet_length = 0
    if 'width' in request.POST:
        carpet_width = int(request.POST['width'])
    if 'length' in request.POST:
        carpet_length = int(request.POST['length'])
    bag = request.session.get('bag', {})

    if carpet_width and carpet_length:
        carpet_area = str(carpet_width * carpet_length)
        if item_id in list(bag.keys()):

            if carpet_area in bag[item_id]['item_measurements'].keys():
                bag[item_id]['item_measurements'][carpet_area] += quantity
                messages.success(request, f'Updated { product.name } quantity to {bag[item_id]["item_measurements"]}')
                # Note - this isn't working properly, need to fix it so that it updated quantity if two of the same size carpets are added to bag
            else:
                bag[item_id]['item_measurements'][carpet_area] = quantity
                messages.success(request, f'Added { product.name } to your bag')
        else:
            bag[item_id] = {'item_measurements': {
                carpet_area : quantity
                }}
            messages.success(request, f'Added { product.name } to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated { product.name } quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added { product.name } to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        carpet_area = None
        if 'carpet_area' in request.POST:
            carpet_area = request.POST['carpet_area']
        bag = request.session.get('bag', {})

        if carpet_area:
            del bag[item_id]['item_measurements'][carpet_area]
            if not bag[item_id]['item_measurements']:
                bag.pop(item_id)
            messages.success(request, f'Removed { product.name } { carpet_area }M² from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed { product.name } from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e:
        messages.error(request, f'Error removing item')
        return HttpResponse(status=500) 
