from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Video(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    video=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(max_length=1000,null=True)
    channel_title=models.CharField(max_length=400,null=True)
    video_image=models.CharField(max_length=400,null=True)

    def __str__(self):
        return self.video

class Comment(models.Model):
    video=models.ForeignKey(Video,on_delete=models.CASCADE,null=True,blank=True)
    comment=models.CharField(max_length=200,null=True)
    text=models.TextField(max_length=1000,null=True)
    writer=models.TextField(max_length=200)
    like_count=models.IntegerField()
    reply_count=models.IntegerField()
    writer_url=models.TextField(max_length=200,null=True)
    writer_image=models.TextField(max_length=200,null=True)
    zorbalık=models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.comment