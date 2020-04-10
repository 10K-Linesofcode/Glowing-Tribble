from django.conf.urls import url
from cbv_app import views

app_name= 'cbv_app'


urlpatterns = [

    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^$',views.SchoolDetailVeiw.as_view(),name=''),
]
