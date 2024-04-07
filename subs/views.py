from django.shortcuts import render

# Create your views here.
def subs(request):
    """ 
    A view to return an index page
    """
    return render(request, 'subs/subs.html')