from django.shortcuts import render

from clubadmin.models import News

# Create your views here.
def index(request):
    """ 
    A view to return an index page
    """
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'home/index.html', context)