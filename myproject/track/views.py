from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Track
# Create your views here.
def alltracks(request):
    tracks = Track.objects.all()
    return render(request, 'track/list.html', {'tracks': tracks})
def gettrackbyid (request,id):
    return HttpResponse(f'<h1>Hallo from get track by id={id}</h1>')
def inserttrack(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Track.objects.create(name=name, description=description)
    return render(request, 'track/insert.html')
def deletetrack(request, id):
    track = get_object_or_404(Track, id=id)
    track.delete()
    return HttpResponse(f'<h1>Track with id={id} has been deleted.</h1>')

def updatetrack(request, id):
    track = get_object_or_404(Track, id=id)

    if request.method == 'POST':
        track.name = (request.POST.get('name') or '').strip()
        track.description = (request.POST.get('description') or '').strip()
        track.save()
        return redirect('alltracks')

    return render(request, 'track/update.html', {'track': track})

