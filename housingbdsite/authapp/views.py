from django.shortcuts import render
from authapp.forms import MusicianForm, AlbumForm
from authapp.models import Person, Album
# Create your views here.

def musician_list(request):
    musicians = Person.objects.all()
    album_lists = Album.objects.all()
    dict = {'musicians': musicians,'album_lists': album_lists}
    return render(request, 'authapp/musician_list.html', context=dict )

def add_musician(request):
    musician_form = MusicianForm()
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)

        if musician_form.is_valid():
            musician_form.save(commit=True)
            return musician_list(request)
    diction = {'musician_form': musician_form}
    return render(request, 'authapp/musician_add.html', context=diction)


# def album_list(request):
#     album_lists = Album.objects.all()
#     return render(request, 'authapp/musician_list.html', {'album_lists': album_lists})


def add_album(request):
    album_form = AlbumForm()

    if request.method == 'POST':
        album_form = AlbumForm(request.POST)

        if album_form.is_valid():
            album_form.save(commit=True)
            return musician_list(request)
    diction = {'album_form': album_form}
    return render(request, 'authapp/album_add.html', context=diction)

def album_list(request):
    return render(request, 'authapp/album_list.html', {})

