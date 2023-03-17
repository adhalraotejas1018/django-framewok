from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    data={   'name':"RutVikk",
              'age':'21',    }
    return render(request,'about.html',data)