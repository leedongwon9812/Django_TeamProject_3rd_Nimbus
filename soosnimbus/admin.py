from django.contrib import admin

# Register your models here.
from .models import Music, User, Playlist, Comment

admin.site.register(Music)
admin.site.register(User)
admin.site.register(Playlist)
admin.site.register(Comment)