from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from .import models
#from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return render(request,'index.html')

#class CBView(View):
#    def get(self, request):
#        return HttpResponse("Class based View")

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']="Basic Injection"
        return context



class SchoolListView(ListView):
    #context_object_name='school_list'
    model= models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'cbv_app/school_detail.html'
