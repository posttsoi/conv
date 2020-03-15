from django.urls import path
from .views import home_page
from .views import convert

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', home_page),
                  path('convert/', convert, name='convert'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
