from django.shortcuts import render

from .models import Fixture

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