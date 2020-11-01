from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeerForm







# Create your views here.
def employeer(request):
    if request.method == 'POST':
        form_data = EmployeerForm(request.POST)

        if form_data.is_valid():
            print(form_data)
            data = form_data.cleaned_data
            print(data)
            print(data['username'])


    form = EmployeerForm()
    context = {
        'form':form
    }
    return render(request,'employeer/employeer.html',context)

    # if request.method = request.POST:
    #     data = request.POST
    #     print(data)
    #     # Two ways of accessing dictionary key value pairs
    #     print(data['email'])
    #     print(data.get('email'))
    #     return render(request,'employeer/employeer.html')
    # else:
    #     return render(request,'employeer/employeer.html')
