import traceback

from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from cart.models import *
from dashboard.forms import LoginForm
from django.core.context_processors import csrf

from cart.cart_manager import CartManager
from cart.models import *

@login_required
def home(request):
    """
    home page view for the website
    """
    categories = Category.objects.all()
    return show_category(request, categories[0].id)

def show_category(request, catid=None):
    """
    category list page view for the website
    """
    sub_categories = []
    try:
        if catid:
            category = Category.objects.get(id=catid)
            products = Product.objects.filter(category=category)
    except:
        pass

    c = {'categories': Category.objects.all(), 'products': products}
    return render_to_response('index.html', c)

def login_page(request):
    """
    If user is authenticated, direct them to the next page. 
    Otherwise, take them to the login page.

    :param request: django HttpRequest

    :return: django HttpResponse 
    """

    state = ""
    username = password = ''
    form = LoginForm()

    #default next page is index page
    next_page = "/"

    #getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        form = LoginForm(request.POST) # A form bound to the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect(next_page) # Redirect after POST
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    c = {'state':state, 'username': username, 'form': form, 'next': next_page}
    c.update(csrf(request)) 

    return render_to_response('auth.html', c)

def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request':request})


def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cm = CartManager(request)
    cm.add(product, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cm = CartManager(request)
    cm.remove(product)

def get_cart(request):
    return render_to_response('cart.html', dict(cart=CartManager(request)))
