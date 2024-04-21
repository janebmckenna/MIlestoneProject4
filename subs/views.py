from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SubsForm
from .models import TeamSubs
from clubadmin.models import Team, Player
from kit.models import Product


def subs(request):
    """
    View for add subs page
    """
    teams = Team.objects.all()
    players = Player.objects.all()
    products = Product.objects.all()

    template = 'subs/subs.html'
    context = {
        'teams': teams,
        'players': players,
        'products': products,
    }

    return render(request, template, context)


@login_required
def all_subs(request):
    """
    Admin screen view all subs
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    players = Player.objects.all()
    teams = Team.objects.all()
    subs = TeamSubs.objects.all().order_by('date')
    on_admin_page = True

    context = {
        "players": players,
        "teams": teams,
        "subs": subs,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'subs/all_subs.html', context)


@login_required
def add_subs(request):
    """
    View for add subs page (manually)
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    on_admin_page = True

    if request.method == 'POST':
        form = SubsForm(request.POST, request.FILES)
        if form.is_valid():
            subs = form.save()
            messages.success(request, 'Subs added successfully!')
            return redirect(reverse('club_admin'))
        else:
            messages.error(request, '''
                New Subs have not been added.
                Please check the form is valid''')
    else:
        form = SubsForm()
    template = 'subs/add_subs.html'
    context = {
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)
