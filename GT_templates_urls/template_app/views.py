from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict={'text':'Hello world', 'number':1000}
    return render(request,'templates_app/index.html',context=context_dict)

def others(request):
    return render(request,'templates_app/others.html')

# def base(request):
#     return render(request,'templates_app/base.html')

def relative(request):
    return render(request,'templates_app/relative_url_template.html')
