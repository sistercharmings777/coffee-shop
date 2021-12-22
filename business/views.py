from django.shortcuts import render


def index(request):
    return render (request, "business/index.html")

def about(request):
    return render (request, "business/about.html")

def product(request):
    return render (request, "business/products.html")

def store(request):
    return render (request, "business/store.html")






























