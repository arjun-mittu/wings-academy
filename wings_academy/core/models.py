from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
class Blog(models.Model):
    title=models.CharField(max_length=255)
    cover_image=models.ImageField()
    content=RichTextField(blank=True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('core:home')
        

class comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    by=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.by)