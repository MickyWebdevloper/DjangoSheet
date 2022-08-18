from django.shortcuts import render, HttpResponseRedirect
from . models import Post
# from . models import Contact
from users.forms import ContectForm


# Home.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# About.


def about(request):
    return render(request, 'blog/about.html')

# About.


def contact(request):
    if request.method == 'POST':
        form = ContectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ContectForm()
    return render(request, 'blog/contact.html', {'form': form})
