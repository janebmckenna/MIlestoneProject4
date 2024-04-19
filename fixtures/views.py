from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Fixture
from .forms import FixtureForm

# Create your views here.

def fixtures(request):
    """ 
    Show all fixtures
    """

    fixtures = Fixture.objects.all().order_by('date')

    context = {
        "fixtures" : fixtures,
    }
    return render(request, 'fixtures/fixtures.html', context)


@login_required
def add_fixture(request):
    """ 
    Add a Fixture
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    on_admin_page = True 

    if request.method == 'POST':
        form = FixtureForm(request.POST, request.FILES)
        if form.is_valid():
            fixture = form.save()
            messages.success(request, 'Fixture added successfully!')
            return redirect(reverse('club_admin'))
        else:
            messages.error(request, 'Fixture has not been added. Please check the form is valid')
    else:
        form = FixtureForm()
    template = 'fixtures/add_fixture.html'
    context ={
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)