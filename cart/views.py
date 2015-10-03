from django.shortcuts import render

@login_required
def home(request):
    """
    home page view for the website
    """
    return render_to_response('index.html')
