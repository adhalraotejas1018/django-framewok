from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    data={ 'name':name,'age':age }
    return render(request,'about.html',data)