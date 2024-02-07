from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('search', search_view, name='main')
]
