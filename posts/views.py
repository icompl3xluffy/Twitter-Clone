from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            #yes, Save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
           #No, Show Error
            return HttpResponseRedirect(form.erros.as_json())




    # Get all post, limit = 20
    posts=Post.objects.all().order_by('-created_at')[:20]

    #show
    return render( request, 'posts.html',
                  {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, "edit.html",{"post":post})
    
x = 0
def LikeView(request, post_id):
    global x
    post = Post.objects.get(id= post_id)
    if x == 0:
        post.liked = 1
        x = 1
    elif x == 1:
        post.liked = 0
        x= 0
    post.save()
    return HttpResponseRedirect('/')   
