from django import urls
from django.conf.urls import url

from myapp.views import index
urlpatterns=[
 url(r'^$',index),
#url(r'^$',index_withTemplate),
]
