from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    n1=int(request.GET.get('num1'))
    n2=int(request.GET.get('num2'))
    result=n1+n2
    data={ 'name':n1,'age':n2 ,'result':result}
    return render(request,'about.html',data)