from django.shortcuts import render, HttpResponse,redirect
from gr.models import Posts,Comment
from django.contrib import messages
from gr.templatetags import extras

# Create your views here.
def grHome(request):
    allposts= Posts.objects.all()
    context={'allposts':allposts}
    return render(request, 'gr/grHome.html',context)
    

def grPost(request,slug):
    post=Posts.objects.filter(slug=slug).first()
    comments=Comment.objects.filter(post=post,parent=None)
    replies=Comment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.sno not in repDict.keys():
            repDict[reply.parent.sno]=[reply]
        else:
            repDict[reply.parent.sno].append(reply)
    context={'post':post,'comments':comments ,'user':request.user,'repDict':repDict}
    return render(request, 'gr/grPost.html',context)

def postComment(request):
    if request.method=='POST':
        comments=request.POST.get("comments")
        user=request.user
        postSNO=request.POST.get("postSNO")
        post=Posts.objects.get(sno=postSNO)
        parentsno=request.POST.get("parentsno")

        if parentsno=="":
            comments=Comment(comments=comments,user=user,post=post)
            comments.save()
            messages.success(request,"comment added")

        else:
            parent=Comment.objects.get(sno=parentsno)
            comments=Comment(comments=comments,user=user,post=post,parent=parent)
            comments.save()
            messages.success(request,"reply added")
    
    return redirect('/gr/{post.slug}')

