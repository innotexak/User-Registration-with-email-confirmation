from django.urls import path

from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns +=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)