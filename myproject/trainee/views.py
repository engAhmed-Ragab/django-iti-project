from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Trainee
from track.models import Track
# Create your views here.
def alltrainees(request):
    context = {}
    context['trainees'] = Trainee.objects.all()
    return render(request,'trainee/list.html',context)
def gettraineebyid (request,id):
    return HttpResponse(f'<h1>Hallo from get trainee by id={id}</h1>')
def inserttrainee(request):
    if request.method == 'POST':
        name     = request.POST.get('Trainee')
        email    = request.POST.get('Email')
        image    = request.FILES.get('Image')
        track_id = request.POST.get('Track')   

        track = get_object_or_404(Track, id=track_id)
        Trainee.objects.create(name=name, email=email, image=image, trackid=track)
    

    context={}
    context['tracks']=Track.getalltracks()
    return render(request, 'trainee/insert.html', context)
def deletetrainee(request, id):
    Trainee.objects.filter(id=id).update(status=False)
    return render(request, 'trainee/list.html', {'trainees': Trainee.objects.all()})
def updatetrainee(request, id):
    trainee = Trainee.gettraineebyid(id)
    context={'trainee':trainee}
    tracks  = Track.objects.all().order_by('name')
    track_id = request.POST.get('Track')
    if track_id:
        trainee.trackid = get_object_or_404(Track, id=track_id)

    if request.method == 'POST':
        trainee.name  = (request.POST.get('name') or '').strip()
        trainee.email = (request.POST.get('email') or '').strip()

        if 'image' in request.FILES:
            trainee.image = request.FILES['image']

        trainee.save()

        return redirect('alltrainees')  

    context = {'trainee': trainee}
    return render(request, 'trainee/update.html', {
        'trainee': trainee,
        'tracks': tracks,
    })