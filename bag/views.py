from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ View that returns bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of product to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    carpet_width = None
    if 'width' in request.POST:
        carpet_width = request.POST['width']
    bag = request.session.get('bag', {})

    if carpet_width:
        if item_id in list(bag.keys()):
            if carpet_width in bag[item_id]['items_by_width'].keys():
                bag[item_id]['items_by_width'][carpet_width] += quantity
            else:
                bag[item_id]['items_by_width'][carpet_width] = quantity
        else:
            bag[item_id] = {'items_by_width': {carpet_width: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
