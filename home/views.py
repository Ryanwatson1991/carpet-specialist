from django.shortcuts import render

# Create your views here.

def index(request):
    """View that returns index page"""

    return render(request, 'home/index.html')


def contact(request):
    """View that returns contact page - have put this in home app as it's something pretty small that I didn't want to create a new app for"""

    return render(request, 'home/contact.html')
