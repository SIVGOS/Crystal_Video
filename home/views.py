from django.shortcuts import render
from django.http import HttpResponse
from uploader.models import Videos

def home(request):
    videos = Videos.objects.all()
    return render(request, 'home_page.html', {'videos': videos[::-1]})

