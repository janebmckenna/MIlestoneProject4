from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found, server_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('kit/', include('kit.urls')),
    path('bag/', include('bag.urls')),
    path('subs/', include('subs.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('clubadmin/', include('clubadmin.urls')),
    path('fixtures/', include('fixtures.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
handler500 = server_error
