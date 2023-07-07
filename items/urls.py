from django.urls import path

from items.views import *

app_name = 'items'

urlpatterns = [
    path('<int:pk>/', detail, name='detail')
]