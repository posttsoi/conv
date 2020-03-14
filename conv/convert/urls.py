from django.urls import path
from .views import home_page
from .views import convert


urlpatterns = [
    path('', home_page),
    path('convert/', convert, name='convert'),
]