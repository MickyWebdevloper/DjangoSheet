from django.shortcuts import render

# Create your views here.


# Home Route
def home(request):
    context = {
        'title': 'Hello world dud, what the hell is going on ha'
    }
    return render(request, 'blog/home.html')
    # return render(request, 'blog/home.html', context)