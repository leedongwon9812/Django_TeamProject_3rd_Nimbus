from django.db import models

# Create your models here.
class Music(models.Model):
    mphoto = models.ImageField(null=True,upload_to='upload/image', blank=True)
    mp3 = models.FileField(upload_to='upload/music')
    mtitle = models.CharField(max_length=45)
    msinger = models.CharField(max_length=45)
    mdesc = models.TextField(blank=True)
    mgenre = models.CharField(max_length=15)
    uemail = models.ForeignKey('User', on_delete=models.CASCADE)
    mrdate = models.DateTimeField()
    mudate = models.DateTimeField()
    mview = models.IntegerField(default=0)
    
class User(models.Model):
    uemail = models.EmailField(primary_key=True, max_length=30)
    uname = models.CharField(max_length=12)
    upwd = models.CharField(max_length=12)
    unick = models.CharField(max_length=30, unique=True)
    urdate = models.DateTimeField()
    uimage = models.ImageField(null=True,upload_to='upload/profile', blank=True)
    utel = models.CharField(max_length=11)
    udesc = models.CharField(max_length=1000)
    def __str__(self):
        return self.uemail
    
class Playlist(models.Model):
    uemail = models.ForeignKey('User', on_delete=models.CASCADE)
    mid = models.ForeignKey('Music', on_delete=models.CASCADE)
    pname = models.CharField(max_length=40)
    
class Comment(models.Model):
    uemail = models.ForeignKey('User', on_delete=models.CASCADE)
    mid = models.ForeignKey('Music', on_delete=models.CASCADE)
    cdesc = models.TextField()
    crdate = models.DateTimeField()