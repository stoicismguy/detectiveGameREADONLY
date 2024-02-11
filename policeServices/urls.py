from django.urls import path
from .views import *

urlpatterns = [
    # path('', database_view, name='main'),
    path('database/', database_view, name='database'),
    path('signatures/', signature_view, name='signatures')
]
