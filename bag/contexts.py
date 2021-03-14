from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Delivery on this site is a flat cost of £20. Grnd total was rendering as £20 all the time so have added the below else statement to set it to '0'
    if total: 
        grand_total = delivery + total
    else: 
        grand_total = 0

    context={
        'bag_items': bag_items,
        'total' : total,
        'product_count' : product_count,
        'delivery' : delivery,
        'free_delivery_delta' : free_delivery_delta,
        'free_delivery_threshold' : settings.FREE_DELIVERY_THRESHOLD,
        'grand_total' : grand_total,
        

    }

    return context
