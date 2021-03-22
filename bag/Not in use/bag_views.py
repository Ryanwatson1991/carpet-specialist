def adjust_bag(request, item_id):
    """ Change quantity of item that is in the bag"""

    quantity = int(request.POST.get('quantity'))
    carpet_width = 0
    carpet_length = 0
    if 'width' in request.POST:
        carpet_width = int(request.POST['width'])
    if 'length' in request.POST:
        carpet_length = int(request.POST['length'])
    bag = request.session.get('bag', {})

    if carpet_width and carpet_length:
        carpet_area = carpet_width * carpet_length
        if quantity > 0:
            bag[item_id]['item_measurements'][carpet_area] = quantity
        else:
            del bag[item_id]['item_measurements'][carpet_area]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

