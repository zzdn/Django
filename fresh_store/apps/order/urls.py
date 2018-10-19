
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^place_order$',place_order)
]
