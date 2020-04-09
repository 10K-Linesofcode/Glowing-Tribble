from django import urls
from django.conf.urls import url

from myapp import views


#Template URLS!!!!!

app_name = 'myapp'


urlpatterns=[
 # url(r'^$',index),
 url(r'^register/$',views.register,name = 'register')
#url(r'^$',index_withTemplate),
]
