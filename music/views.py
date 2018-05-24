from django.shortcuts import render_to_response
from django.template import RequestContext
from Radio.models import Song, Artist, Album

def SpecificSong(request, songname):
    song = Song.objects.get(songName = songname)
    context = {'song':song}
    return render_to_response('specificsong.html',context, context_instance=RequestContext(request)
