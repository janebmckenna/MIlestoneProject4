from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def club_admin(request):
    """ 
    A view to return an index page
    """
    if not request.user.is_superuser:
        message.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))
    return render(request, 'clubadmin/club_admin.html')