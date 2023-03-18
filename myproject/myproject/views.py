from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    fname=request.POST.get('fname',"first_name not enter")
    lname=request.POST.get('lanme',"last_name not enter")
    about_self=request.POST.get('textarea',"about not enter")
    data={'fname':fname,
          'lname':lname,
          'about_self':about_self}
    return render(request,'about.html',data)