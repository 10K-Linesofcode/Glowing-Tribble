from django.conf.urls import url
#from first_app.views import index
#from GT_app.views import index_withTemplate
from GT_app.views import index
urlpatterns=[
 url(r'^$',index),
#url(r'^$',index_withTemplate),
]
