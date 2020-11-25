from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils.text import slugify
import itertools
is_paid=(("paid","paid"),
          ("free","free"))

class course(models.Model):
    title=models.CharField(max_length=255)
    short_description=models.TextField(blank=False)
    description=models.TextField(blank=False)
    type=models.CharField(choices=is_paid,default='free',max_length=10)
    created_on=models.DateTimeField(auto_now_add=True)
    cover_img=models.ImageField(null=True)
    def __str__(self):
        return self.title

class lessons(models.Model):
    course=models.ForeignKey(course, on_delete=models.CASCADE)
    title=models.CharField(max_length=255,blank=False)
    description=models.TextField(blank=False)
    video=models.FileField(upload_to="courses/",null=False)
    
    