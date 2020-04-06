from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from GT_app.models import Topic,Webpage,AccessRecord


# Create your views here.

#def index(request):
#     return HttpResponse(' Hello World')
#     pass
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'index.html',context=date_dict)

#def index_withTemplate(request):
#    insert_dict= {'insert_me':'Hello im comming from  views.py'}
#    return render(request,'index.html',insert_dict)
