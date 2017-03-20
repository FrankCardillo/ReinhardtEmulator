from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_title
