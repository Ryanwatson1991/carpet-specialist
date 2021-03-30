from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ Allows bag contents to be accessed accross the site """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        # If product does not have size requirements, add the following to bag
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            # If product does have size requirements, add the following
            #  - uses specified carpet_area to calculate price. 
            product = get_object_or_404(Product, pk=item_id)
            for carpet_area, quantity in item_data[
                                        'item_measurements'].items():
                carpet_price = product.price * int(carpet_area)
                total += quantity * carpet_price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'carpet_area': carpet_area,
                    'carpet_price': carpet_price,
                })

# Calculates whether delivery should be charged. 
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Delivery on this site is a flat cost of £20. Grnd total was rendering as
    # £20 all the time so have added the below else statement to set it to '0'
    if total: 
        grand_total = delivery + total
    else: 
        grand_total = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context