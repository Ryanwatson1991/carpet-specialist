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
    carpet_colour = None
    if 'width' in request.POST:
        carpet_width = int(request.POST['width'])
    if 'length' in request.POST:
        carpet_length = int(request.POST['length'])
    if 'colour' in request.POST:
        print("COLOUR IS IN REQUEST")
        carpet_colour = request.POST['colour']
        print(f"CARPET_COLOUR: {carpet_colour}")
    bag = request.session.get('bag', {})

    if carpet_width and carpet_length:
        carpet_area = str(carpet_width * carpet_length)
        '''carpet_details = {
                'carpet_area' : carpet_area,
                'carpet_colour' : carpet_colour
            }
        print(carpet_details)'''
        if item_id in list(bag.keys()):
            if carpet_area in bag[item_id]['item_measurements'].keys():
                # If carpet with specified area is already in bag, update quantity
                bag[item_id]['item_measurements'][carpet_area] += quantity
                messages.success(request, f'Updated { product.name } quantity to {bag[item_id]["item_measurements"]}')
            else:
                # If carpet with different area is in the bag, add carpet with new area as different item to bag
                bag[item_id]['item_measurements'][carpet_area] = quantity
                messages.success(request, f'Added { product.name } to your bag')
        else:
            # If carpet isn't already in bag, add totally new item to bag
            bag[item_id] = {'item_measurements': {
                carpet_area : quantity,
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
