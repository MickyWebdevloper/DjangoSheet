from distutils.archive_util import make_archive
from django.contrib import auth
from django.http.response import HttpResponseRedirect
# uper geeky
from django.shortcuts import render
from django.contrib import messages
# as auth_login, as auth_logout i write cuz login, logout module same name as my function name
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from . forms import SignUpForm, LoginForm, PostForm, UpdatePostForm
from blog.models import Post
from django.contrib.auth.models import Group

# signup geeky shows


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Congratulations! {username} You Become An Author')
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            # redirect to a new URL:
            return HttpResponseRedirect('/users/login/')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


# login -- Geeky Shows
# login required --> coreyMS --> here i can also use
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST, data=request.POST)
            if form.is_valid():
                # form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    messages.success(
                        request, f'{username} Successfully Loged In!')
                    return HttpResponseRedirect('/users/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/users/dashboard/')


# login required --> coreyMS
# logout
@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


# login required --> coreyMS
# dashboard
@login_required
def dashboard(request):
    context = {
        'posts': Post.objects.all(),
        'full_name': request.user.get_full_name(),
        'gps': request.user.groups.all()
    }
    return render(request, 'users/dashboard.html', context)


# login required --> coreyMS
# dashboard Add_post
@login_required
def add_post(request):
    if request.method == 'POST':
        print('Post method inside ...............')
        form = PostForm(request.POST)
        if form.is_valid():
            print('Post Validation inside ...............')
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            posts = Post(title=title, content=content)
            posts.save()
            print('Post Validation After ...............')
            messages.success(
                request, 'Successfully Posted!')
            return HttpResponseRedirect('/users/dashboard/')
    else:
        form = PostForm()
    return render(request, 'users/add_post.html', {'form': form})


# login required --> coreyMS
# dashboard Update_post
@login_required
def update_post(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        form = UpdatePostForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully Updated! Post')
            return HttpResponseRedirect('/users/dashboard/')
    else:
        pi = Post.objects.get(pk=id)
        form = UpdatePostForm(instance=pi)
    return render(request, 'users/update_post.html', {'form': form})

# login required --> coreyMS
# dashboard Delete_post


@login_required
def delete_post(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
        messages.success(
            request, 'Successfully Deleted! Post')
        return HttpResponseRedirect('/users/dashboard/')
    else:
        return render(request, 'users/update_post.html')