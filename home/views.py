

from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from gr.models import Posts

# Create your views here.
# html pages
def home(request):
    return render(request, 'home/home.html')
    
def about(request):
    return render(request, 'home/about.html')

def news(request):
    return render(request, 'gr/grPost.html')
   
def contact(request):
    
    if request.method=='POST':
        email=request.POST['emailID']
        sug=request.POST['sug']
        print(email,sug)

        if len(sug)<4 or len(email)<4:
            messages.error(request,"Please fill correctly")
        else:
            contact=Contact(email=email,sug=sug)
            contact.save()
            messages.success(request,"Your message has been sent")
        
    return render(request, 'home/contact.html')

def search(request):
    # allPosts=Posts.objects.all()
    search=request.GET['search']
    allPosts=Posts.objects.filter(title__icontains=search)
    # allPostscontent=Posts.objects.filter(content__icontains=search)
    # allPosts=allPosts.union(allPostscontent)
    params={'allPosts':allPosts}
    return render(request, 'home/search.html',params)


# authentication apis 
def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        Addr=request.POST['Addr']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']

        #create user
        myuser=User.objects.create_user(username,email,password)
        myuser.Address=Addr
        myuser.city=city
        myuser.state=state
        myuser.zip=zip
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect("/")


    else:
        return HttpResponse('404 - Not found')


def handleLogin(request):
    if request.method=='POST':
        lusername=request.POST['lusername']
        lpassword=request.POST['lpassword']

        user=authenticate(username=lusername,password=lpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect("/")
        
        else:
            messages.error(request,"Invalid credentials")

    # return HttpResponse('handleLogin')
    return HttpResponse('404 - Not found')

def handleLogout(request):

    logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect("/")

    #return HttpResponse('handleLogout') 
