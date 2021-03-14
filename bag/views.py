from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """View that returns index page"""

    return render(request, 'bag/bag.html')