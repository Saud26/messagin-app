from authsystem.models import customer
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


# Files from other apps
from authsystem.models import customer 

# Create your views here.

from .decorators import authorizedUsersCanView
from .forms import SubmitPostForm
from .models import Post

@authorizedUsersCanView
def homePage(request):

    form = SubmitPostForm(request.POST)
    posts = Post.objects.all()

    context = {'posts': posts, 'form': form}
    return render(request, 'posts/main.html', context)

@authorizedUsersCanView
def submit_post(request):
    instance = customer.objects.filter(user=request.user).first()
    form = SubmitPostForm(request.POST, instance=instance)


    if request.method == 'POST':
        form = SubmitPostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('posts:homePage')
        else:
            messages.error(request, 'Error while saving your post. Try again')

    context = {'form': form}
    return render(request, 'posts/post_form.html', context)

@authorizedUsersCanView
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        form = SubmitPostForm(instance=post)

        if request.method == 'POST':
            form = SubmitPostForm(request.POST, instance=post)

            if form.is_valid():
                form.save()
                return redirect('posts:homePage')

        context = {'form':form}
        return render(request, 'posts/post_form.html', context)
    else:
        return redirect('posts:homePage')

@authorizedUsersCanView
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted Successfully.')
        return redirect('posts:homePage')

    context = {'post':post}
    return render(request, 'posts/delete.html', context)