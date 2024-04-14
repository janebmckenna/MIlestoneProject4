from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from kit.models import Product


@login_required
def club_admin(request):
    """ 
    A view for club admin actions
    """
    if not request.user.is_superuser:
        message.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))
    return render(request, 'clubadmin/club_admin.html')


@login_required
def edit_delete_admin(request):
    """ 
    A simplified view for edit/delete items
    """
    if not request.user.is_superuser:
        message.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    products = Product.objects.all()
    on_admin_page = True
    
    context = {
        "products" : products,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/edit_delete_admin.html', context)