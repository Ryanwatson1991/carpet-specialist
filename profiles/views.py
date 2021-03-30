from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please confirm details have been entered correctly.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    products = Product.objects.filter(favourite=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'products': products,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Get user's order history and display on profile page
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A Confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def favourite_product(request, product_id):
    """
    Allows user to favourite products by 
    pressing heart button on product detail page
    """
    product = get_object_or_404(Product, pk=product_id)
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        messages.success(request, f'{product.name}successfully removed from favourites')
    else:
        product.favourite.add(request.user)
        messages.success(request, f'{product.name} successfully added to favourites')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def user_favourites(request):
    """
    Displays user's favourites on profile page
    """
    products = Product.objects.filter(favourite=request.user)

    return render(request)
