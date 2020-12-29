from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    context = {'success': False}
    if request.method == "POST":
        if request.user.is_authenticated:
            current_user = request.user
            id = current_user.id
            task_title = request.POST['title']
            task_desc = request.POST['desc']

            ins = task(task_title=task_title, task_desc=task_desc,user_id=id)
            ins.save()

            context = {'success': True}
        else:
            messages.error(request,"You need to be logged in")
            return redirect('Home')

    return render(request, 'index.html', context)


def list(request):

    # add objects = models.Manager() to ignore error
    # filter data
    # allTasks = task.objects.filter(id__contains='2')
    # order data
    # allTasks = task.objects.order_by('-id')
    if request.user.is_authenticated:
        current_user = request.user
        id = current_user.id
        
        allTasks = task.objects.filter(user_id=id).filter(task_complete=0)
        completeTasks = task.objects.filter(user_id=id).filter(task_complete=1)
        context = {'tasks': allTasks,'completeTasks':completeTasks}
        return render(request, 'list.html', context)
    else:
        messages.error(request,"You need to be logged in")
        return redirect('Home')

def delete(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            task_serial_id = request.POST['id']
            ins = task.objects.filter(id= task_serial_id)
            ins.delete()
            messages.success(request,"Task Deleted!")
            return redirect('list')
        else:
            messages.error(request,"You need to be logged in")
            return redirect('Home')


def update(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            task_serial_id = request.POST['id']

            ins = task.objects.get(id= task_serial_id)
            ins.task_complete = 1
            ins.save()
            messages.success(request,"Task Complete!")
            return redirect('list')
        else:
            messages.error(request,"You need to be logged in")
            return redirect('Home')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        if User.objects.filter(username=name):
            messages.error(request, "This Username is Exits!")

            return redirect('Home')

        if password == conpassword:
            # create user
            myuser = User.objects.create_user(name, email, password)
            myuser.save()
            context = {'registerSuccessful': True}
            return render(request, 'index.html', context)
        else:
            messages.error(request, "password Does Not Match")

            return redirect('Home')

        
    else:
        return HttpResponse('404- Not Allowed')


def handlelogin(request):

   if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('Home')
        else:
            messages.error(request,"Invalid Credentials!")
            return redirect('Home')


def handlelogout(request):

    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('Home')
