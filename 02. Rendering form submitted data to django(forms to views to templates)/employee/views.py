from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request,'home.html')

context = {
    'ceo':{
                'name':'Netra Prasad Neupane',
                'gender':'Male'
    },
    'hr':{
                'name':'Hari Neupane',
                'gender':'Female'
    }
}

def employee(request):
    return render(request,'employee/employee.html',context)

def about(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        context_ ={
            'title':'employeer',
            'email': email,
            'password':password

        }


    else:
        context_ ={
            'title':'employeer',
            'email':'None',
            'password':'None'
            }

    return render(request,'about.html',context_)




def contact(request):
    return render(request,'contact.html')
