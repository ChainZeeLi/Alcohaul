from django.conf.urls import url
from . import views

urlpatterns = [

	#/storage/
    url(r'^$', views.index, name='index'),
    # storage/beer
    url(r'^(?P<alcohol_name>[a-zA-Z0-9]+)/$', views.detail, name='detail'),



]



