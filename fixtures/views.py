from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from datetime import date

from .models import Fixture
from .forms import FixtureForm


def fixtures(request):
    """
    Show all fixtures
    """
    today = date.today()
    fixtures = Fixture.objects.all().order_by('date')

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(
                request, "You didn't enter any search parameters!")
            return redirect(reverse('fixtures'))

        queries = Q(
            team__icontains=query) | Q(
                opponent__icontains=query) | Q(date__icontains=query)
        fixtures = fixtures.filter(queries)

    context = {
        "fixtures": fixtures,
        'today': today,
    }
    return render(request, 'fixtures/fixtures.html', context)


@login_required
def add_fixture(request):
    """
    Add a Fixture
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    on_admin_page = True

    if request.method == 'POST':
        form = FixtureForm(request.POST, request.FILES)
        if form.is_valid():
            fixture = form.save()
            messages.success(request, 'Fixture added successfully!')
            return redirect(reverse('club_admin'))
        else:
            messages.error(request, '''
                Fixture has not been added. Please check the form is valid''')
    else:
        form = FixtureForm()
    template = 'fixtures/add_fixture.html'
    context = {
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)


@login_required
def manage_fixtures(request):
    """
    A simplified view for edit/delete fixtures
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    today = date.today()
    fixtures = Fixture.objects.all().order_by('date')
    on_admin_page = True

    context = {
        "fixtures": fixtures,
        'today': today,
        'on_admin_page': on_admin_page,
    }
    return render(request, 'fixtures/fixtures_manage.html', context)


@login_required
def delete_fixture(request, fixture_id):
    """
    Delete a Fixture
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=fixture_id)
    fixture.delete()
    messages.success(request, 'Fixture has been deleted!')

    return redirect(reverse('manage_fixtures'))


@login_required
def edit_fixture(request, fixture_id):
    """
    Edit an exisiting Fixture
    """
    if not request.user.is_superuser:
        messages.error(request, '''
            Sorry. This action requires club admin access''')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=fixture_id)
    if request.method == 'POST':
        form = FixtureForm(request.POST, request.FILES,  instance=fixture)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fixture successfully updated')
            return redirect(reverse('manage_fixtures'))
        else:
            messages.error(request, '''
                Fixture has not been updated, please check form is valid.''')
    else:
        form = FixtureForm(instance=fixture)

    template = 'fixtures/edit_fixture.html'
    context = {
        'form': form,
        'fixture': fixture,
        'on_admin_page': True,
    }

    return render(request, template, context)
