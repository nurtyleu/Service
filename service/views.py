from django.shortcuts import render


def but(request):
    return render(request, 'service/web_development.html')

def mob(request):
    return render(request, 'service/mob_design.html')

def brand(request):
    return render(request, 'service/branding.html')
