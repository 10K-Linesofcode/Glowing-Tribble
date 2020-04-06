from django.shortcuts import render

# Create your views here.

from . import forms


def index(request):
    return render(request, 'form_app/index.html')

def form_name_view(request):
    form=forms.FormName()
    if request.method =='POST':
        form= forms.FormName(request.POST)


        if form.is_valid():
            # Do Something Code
            print(" Validation sucecss")
            print("NAME: "+ form.cleaned_data['name'])
            print("Email: "+ form.cleaned_data['email'])
            print("Text: "+ form.cleaned_data['text'])
    return render (request,'form_app/form_app.html', {'form':form} )
