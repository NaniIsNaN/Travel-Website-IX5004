from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

from traitlets import default

User = get_user_model()
#choices

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    region = models.CharField(max_length=100,default="Kayin")
    language = models.CharField(max_length=100,default='Burmese')
    fst_name = models.CharField(max_length=100,default="mAaLol")
    lst_name = models.CharField(max_length=100,default="MINAUNGHLAING")
    profile_img = models.ImageField(upload_to='profile_images' , default="default.png")
   
    # region = models.CharField(max_length=100,choices=region_choices)
    def __str__(self) -> str:
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image =  models.ImageField(upload_to='post_images')
    caption = models.TextField()
    txt = models.TextField(default=".....")
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user