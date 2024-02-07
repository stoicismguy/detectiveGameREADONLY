from django.urls import path
from .views import *

urlpatterns = [
    path('', desktop_view, name='desktop'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
