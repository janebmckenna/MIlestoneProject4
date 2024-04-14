from django.shortcuts import render

# Create your views here.
def club_admin(request):
    """ 
    A view to return an index page
    """
    return render(request, 'clubadmin/club_admin.html')