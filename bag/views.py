from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ View that returns bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of product to the bag"""

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
        carpet_area = carpet_width * carpet_length
        if item_id in list(bag.keys()):
            if carpet_area in bag[item_id]['item_measurements'].keys():
                bag[item_id]['item_measurements'][carpet_area] += quantity
            else:
                bag[item_id]['item_measurements'][carpet_area] = quantity
        else:
            bag[item_id] = {'item_measurements': {
                carpet_area : quantity,
                }}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
