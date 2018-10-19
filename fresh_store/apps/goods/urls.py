
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^login",login),
    url(r"^register$",register),
    url(r"^list",list),
    url(r"^detail",detail),
    url(r"^index",index),
]


# ../static/