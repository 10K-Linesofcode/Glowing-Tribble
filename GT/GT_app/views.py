from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse


# Create your views here.

# def index(request):
#     return HttpResponse(' Hello World')
#     pass

def index_withTemplate(request):
    insert_dict= {'insert_me':'Hello im comming from  views.py'}
    return render(request,'index.html',insert_dict)
