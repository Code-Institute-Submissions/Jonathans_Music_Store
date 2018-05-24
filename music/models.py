from django.db import models

class Artist(models.Model):
    artistName = models.CharField(max_length = 30)
    artistInfo = models.TextField()

    def __unicode__(self):
        return self.artistName

class Album(models.Model):
    albumName = models.CharField(max_length = 30)
    artist = models.ForeignKey('Artist')
    date = models.DateTimeField('Release Date')
    albumInfo = models.TextField()
    albumArt = models.ImageField(upload_to="images/albumart/")

    def __unicode__(self):
        return self.albumName

  class Song(models.Model):
    songName = models.CharField(max_length = 30)
    artist = models.ForeignKey('Artist')
    album = models.ForeignKey('Album')
    audio_track = models.FileField(upload_to="songs/")

    def __unicode__(self):
        return self.songName