from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'cont2.html')