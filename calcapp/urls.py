from django.conf.urls import url
from calcapp import views

urlpatterns = [
    url(r'^api/calculate$', views.calulate)
]