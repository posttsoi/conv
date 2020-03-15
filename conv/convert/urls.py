from django.urls import path
from .views import home_page


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', home_page, name='home'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
