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
    products = Product.objects.all()

    template = 'subs/subs.html'
    context ={
        'teams': teams,
        'players': players,
        'products': products,
    }

    return render(request, template, context)