from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employeer(request):
    return render(request,'employeer/employeer.html')
