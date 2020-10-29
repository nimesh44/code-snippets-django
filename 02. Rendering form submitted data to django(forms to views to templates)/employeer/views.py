from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employeer(request):
    return render(request,'employeer/employeer.html')

    # if request.method = request.POST:
    #     data = request.POST
    #     print(data)
    #     # Two ways of accessing dictionary key value pairs
    #     print(data['email'])
    #     print(data.get('email'))
    #     return render(request,'employeer/employeer.html')
    # else:
    #     return render(request,'employeer/employeer.html')
