from django.conf.urls import url

from template_app import views

#Template Tagging

app_name = 'template_app'

urlpatterns= [

url(r'^relative/$',views.relative, name = 'relative'),
url(r'^others/$', views.others, name = 'others')

]
