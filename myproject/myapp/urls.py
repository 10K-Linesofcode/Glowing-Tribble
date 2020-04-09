from django import urls
from django.conf.urls import url

from myapp import views


#Template URLS!!!!!

app_name = 'myapp'


urlpatterns=[
 # url(r'^$',index),
 url(r'^register/$',views.register,name = 'register'),
 url(r'^logout/$',views.user_logout,name = 'logout'),
 url(r'special/',views.special,name = 'special'),
 url(r'^user_login/$',views.user_login,name = 'user_login')
#url(r'^$',index_withTemplate),
]
