from django.shortcuts import render, redirect

def redir(request):
    return redirect('home/')

def home_page(request):
    return render(request, "home.html")


def store_page(request):
    return render(request, "store.html")


def aboutus_page(request):
    return render(request, "about_us.html")


def support_page(request):
    return render(request, "support.html")
