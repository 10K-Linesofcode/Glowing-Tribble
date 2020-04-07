from django.shortcuts import render

# Create your views here.


from user_app.models import User

from user_app.forms import NewUserForm

def index(request):
    return render(request, 'user_app/index.html')

# def users(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {'users': user_list}
#     return render(request,'user_app/users.html',context=user_dict)


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print(' Error Form Invalid .......')

    return render(request,'user_app/users.html',{'form':form})
