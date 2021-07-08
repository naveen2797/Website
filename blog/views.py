from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import LoginForm, contactform, PostFrom
from .models import Contact,Post
from django.contrib import messages
from .forms import signupfrom
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm 
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.models import Group
# Create your views here.


def index(request):
    return render(request,'blog/index.html')


def contact(request):
    if request.method == 'POST':
        fm = contactform(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['phone']
            ds = fm.cleaned_data['desc']
            user = Contact(name=nm,email=em,phone=ph,desc=ds)
            user.save()
            fm = contactform()
            messages.success(request, 'You Form submitted!')
        else:
            fm=contactform()    
    else:
        fm = contactform()
    return render(request,'blog/contact.html',{'form':fm})


def about(request):
    return render(request,'blog/about.html')


def signup(request):
    if request.method=='POST':
        fm = signupfrom(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
            messages.success(request,'your account created')
            fm = signupfrom()
    else:
        fm = signupfrom()
    return render(request,'blog/signup.html',{'form':fm})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pswd = fm.cleaned_data['password']
                user = authenticate(username=uname,password=pswd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'you have logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = LoginForm()
        return render(request,'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'blog/profile.html',{'name':request.user,'email':request.user})
    else:
        return HttpResponseRedirect('/login/')



def blogpost(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'blog/bloghome.html',context)


def blogposts(request,Slug):
   posts = Post.objects.filter(Slug=Slug).first()
   context = {'posts':posts}
   return render(request,'blog/blog.html',context)



def update(request,Slug):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(Slug=Slug)
            form = PostFrom(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                form = PostFrom()
                messages.success(request,'Your post updated ')
        else:
            pi = Post.objects.get(Slug=Slug)
            form = PostFrom(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PostFrom(request.POST)
            if fm.is_valid():
                fm.save()
                fm = PostFrom()
        else:
            fm = PostFrom()
        return render(request,'blog/AddPost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


