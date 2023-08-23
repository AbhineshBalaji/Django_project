from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def indexhtml(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def indexhtml1(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def indexhtml2(request):
    template = loader.get_template('task.html')
    return HttpResponse(template.render())

def indexhtml3(request):
    template = loader.get_template('sign.html')
    return HttpResponse(template.render())

def back(request):
    return redirect('indexhtml')

def createuser(request):
    users = request.POST['username']
    password1 = request.POST['password1']
    email = request.POST['email']
    password2= request.POST['password2']

    if password1 == password2:
        load = signup(username = users,password = password1,email = email)
        load.save()
        return redirect('indexhtml')
    else:
        return HttpResponse("pasword are not match")
    
def signin(request):
    email = request.POST['emailid']
    password = request.POST['pass']
    data = signup.objects.filter(email=email)
    if data:
        data = signup.objects.get(email=email)
        if data.password == password:
            return redirect('indexhtml1')
        else:
            return HttpResponse("Wrong password")
    else:
        return HttpResponse("Incorect password")