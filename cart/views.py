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

@login_required
def home(request):
    """
    home page view for the website
    """
    return render_to_response('index.html')
