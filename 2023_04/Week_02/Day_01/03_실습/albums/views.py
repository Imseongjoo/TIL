from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm
from django.conf import settings


# Create your views here.


def index(request):
    albums = Album.objects.all()

    context = {
        'albums': albums,
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'albums/index.html', context)


def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums:index')
    else:
        form = AlbumForm()
    return render(request, 'albums/create.html', {'form': form})
