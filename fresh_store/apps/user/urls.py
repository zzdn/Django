from django.conf.urls import url

from .views import *
urlpatterns = [
    url(r'^user_center_info$',user_center_info),
    url(r'^user_center_order$',user_center_order),
    url(r'^user_center_site$',user_center_site),

]
