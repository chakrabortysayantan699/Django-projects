from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #here i'm passing the name as a dictionary
    return render(request,'index.html',{'name':'PAPON'})
    #return HttpResponse('<h1>Hello world !!</h1>')
def add(request):
    '''
    this will use when we work with GET method
    val1=int(request.GET['num1'])    
    val2=int(request.GET['num2'])
    result=val2+val1
    return render(request,'result.html',{'result':result})

    '''
    #but as we sending data to sever we will use post method
    val1=int(request.POST['num1'])    
    val2=int(request.POST['num2'])
    result=val2+val1
    return render(request,'result.html',{'result':result})
