from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import News, NewsCategory, Team, Player
from .forms import NewsForm, PlayerForm
from kit.models import Product, Category


@login_required
def club_admin(request):
    """
    A view for club admin actions
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))
    return render(request, 'clubadmin/club_admin.html')


@login_required
def edit_delete_admin(request):
    """
    A simplified view for edit/delete items
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    products = Product.objects.all()
    on_admin_page = True

    context = {
        "products": products,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/edit_delete_admin.html', context)


@login_required
def manage_categories(request):
    """
    a view to manage categories
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    categories = Category.objects.all()
    on_admin_page = True

    context = {
        "categories": categories,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/manage_categories.html', context)


@login_required
def add_news(request):
    """
    Add a News Story
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    on_admin_page = True

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            messages.success(request, 'News item added successfully!')
            return redirect(reverse('club_admin'))
        else:
            messages.error(request, '''
                News has not been added. Please check the form is valid''')
    else:
        form = NewsForm()
    template = 'clubadmin/add_news.html'
    context = {
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
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    news = News.objects.all()
    on_admin_page = True

    context = {
        "news": news,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/edit_delete_news.html', context)


@login_required
def delete_news(request, news_id):
    """
    Delete a News article
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    news = get_object_or_404(News, pk=news_id)
    news.delete()
    messages.success(request, 'News Article has been deleted!')

    return redirect(reverse('edit_delete_news'))


@login_required
def edit_news(request, news_id):
    """
    Edit an exisiting news article
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES,  instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, f'{news.title} successfully updated')
            return redirect(reverse('edit_delete_news'))
        else:
            messages.error(request, '''
                This article has not been updated,
                please check form is valid.''')
    else:
        form = NewsForm(instance=news)
        messages.info(request, f'You are editing {news.title}')

    template = 'clubadmin/edit_news.html'
    context = {
        'form': form,
        'news': news,
        'on_admin_page': True,
    }

    return render(request, template, context)


def news_item(request, news_id):
    """
    A view to show individual news pages with full stories
    """

    news = get_object_or_404(News, pk=news_id)

    context = {
        "news": news,
    }
    return render(request, 'clubadmin/news_item.html', context)


def all_news(request):
    """
    A view to show individual news pages with full stories
    """

    news = News.objects.all().order_by('-date')

    context = {
        "news": news,
    }
    return render(request, 'clubadmin/all_news.html', context)


@login_required
def add_player(request):
    """
    Add a Player
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    on_admin_page = True

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save()
            messages.success(request, 'Player added successfully!')
            return redirect(reverse('manage_players'))
        else:
            messages.error(request, '''
                Player has not been added. Please check the form is valid''')
    else:
        form = PlayerForm()
    template = 'clubadmin/add_player.html'
    context = {
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)


@login_required
def manage_players(request):
    """
    Admin screen for managing players
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    players = Player.objects.all()
    on_admin_page = True

    context = {
        "players": players,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'clubadmin/manage_players.html', context)


@login_required
def delete_player(request, player_id):
    """
    Delete a Player
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    player = get_object_or_404(Player, pk=player_id)
    player.delete()
    messages.success(request, 'Player has been deleted!')

    return redirect(reverse('manage_players'))


@login_required
def edit_player(request, player_id):
    """
    Edit an exisiting Player
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES,  instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, f'''
                {player.display_name} successfully updated''')
            return redirect(reverse('manage_players'))
        else:
            messages.error(request, '''
                Player has not been updated, please check form is valid.''')
    else:
        form = PlayerForm(instance=player)
        messages.info(request, f'You are editing {player.display_name}')

    template = 'clubadmin/edit_player.html'
    context = {
        'form': form,
        'player': player,
        'on_admin_page': True,
    }

    return render(request, template, context)
