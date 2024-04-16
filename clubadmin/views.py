from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import News, NewsCategory, Team
from .forms import NewsForm
from kit.models import Product, Category



@login_required
def club_admin(request):
    """ 
    A view for club admin actions
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))
    return render(request, 'clubadmin/club_admin.html')


@login_required
def edit_delete_admin(request):
    """ 
    A simplified view for edit/delete items
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    products = Product.objects.all()
    on_admin_page = True
    
    context = {
        "products" : products,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/edit_delete_admin.html', context)


@login_required
def manage_categories(request):
    """ 
    a view to manage categories
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    categories = Category.objects.all()
    on_admin_page = True
    
    context = {
        "categories" : categories,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/manage_categories.html', context)


@login_required
def add_news(request):
    """ 
    Add a News Story
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    on_admin_page = True 

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            messages.success(request, 'News item added successfully!')
            return redirect(reverse('club_admin'))
        else:
            messages.error(request, 'News has not been added. Please check the form is valid')
    else:
        form = NewsForm()
    template = 'clubadmin/add_news.html'
    context ={
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)


@login_required
def edit_delete_news(request):
    """ 
    A simplified view for editing and deleting news
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    news = News.objects.all()
    on_admin_page = True
    
    context = {
        "news" : news,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/edit_delete_news.html', context)


@login_required
def delete_news(request, news_id):
    """ 
    Delete a News article
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    news = get_object_or_404(News, pk=news_id)
    news.delete()
    messages.success(request, 'News Article has been deleted!')

    return redirect(reverse('clubadmin/edit_delete_news.html'))