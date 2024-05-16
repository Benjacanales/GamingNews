from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'core/index.html')

def noticiaCS1 (request):
    return render(request, 'core/noticiaCS1.html')

def noticiaCS2 (request):
    return render(request, 'core/noticiaCS2.html')

def noticiaCS3 (request):
    return render(request, 'core/noticiaCS3.html')

def noticiaCS4 (request):
    return render(request, 'core/noticiaCS4.html')

def cs2 (request):
    return render(request, 'core/cs2.html')

def lol (request):
    return render(request, 'core/lol.html')

def noticiaLol1 (request):
    return render(request, 'core/noticiaLol1.html')

def noticiaLol2 (request):
    return render(request, 'core/noticiaLol2.html')

def noticiaLol3 (request):
    return render(request, 'core/noticiaLol3.html')

def noticiaLol4 (request):
    return render(request, 'core/noticiaLol4.html')

def login (request):
    return render(request, 'core/login.html')

def loginRegistro (request):
    return render(request, 'core/loginRegistro.html')

    