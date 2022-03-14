from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import PasswordChangeForm
from . models import Blog
from . forms import Edit_Blog
from django.core.mail import send_mail

def index(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request,'home.html',context)



def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.warning(request,'password does not match')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'User registered successfully')
            return redirect('login')

        

    return render(request,'login.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'User is not registered')
            return redirect('register')
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')   


def post_blog(request):
    if request.method=="POST":
        title = request.POST.get('title')
        desc =  request.POST.get('Description')
        blog = Blog(title=title,dsc=desc,user_id=request.user)
        blog.save()
        messages.success(request,'post has been submitted successfully')
        return redirect('post_blog')
    return render(request,'blog_post.html')

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog_detail.html',context)

def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,'Post has been deleted')
    return redirect('/')

def edit(request,id):
     blog = Blog.objects.get(id=id)
     editblog = Edit_Blog(instance=blog)
     if request.method=='POST':

         form = Edit_Blog(request.POST,instance=blog)
         if form.is_valid():

             form.save()
             messages.success(request,'POST has been updated')
             return redirect('/')

     return render(request,'edit_blog.html',{'edit_blog':editblog})
     

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #update_session_auth_hash(request, user)
            messages.success(request,'Your password has been changed')
            return redirect('/')
        else:    
            messages.warning(request,'Error')
            return redirect('change_password')
    else:        
        form = PasswordChangeForm(request.user)
        return render(request,'change_password.html',{'PasswordChangeForm':form})      

