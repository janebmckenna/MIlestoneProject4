from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages

from .forms import SubsForm
from .models import TeamSubs
from clubadmin.models import Team, Player
from kit.models import Product


# Create your views here.
def subs(request):
    """ 
    View for add subs page
    """
    teams = Team.objects.all()
    players = Player.objects.all()
    product = get_object_or_404(Product, pk='9')

    template = 'subs/subs.html'
    context ={
        'teams': teams,
        'players': players,
        'product': product,
    }

    return render(request, template, context)