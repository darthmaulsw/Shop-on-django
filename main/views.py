from django.shortcuts import render,redirect

def redir(request):
    return redirect('home/')

def home_page(request):
    return render(request, "base.html")
