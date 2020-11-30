from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

user_type=(
    ('foundation','foundation'),
    ('mains','mains'),
    ('preliminary','preliminary'),
    ('free','free')
)
class Blog(models.Model):
    title=models.CharField(max_length=255)
    cover_image=models.ImageField()
    content=RichTextUploadingField(blank=True,null=True)
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

class paid(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    type=models.CharField(choices=user_type,default='free',max_length=20)
    
def create_paid(sender,instance,created,**kwargs):
    if created:
        paid.objects.create(user=instance)

post_save.connect(create_paid,sender=User)


class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phoneno=models.CharField(max_length=10)
    msg=models.TextField()
