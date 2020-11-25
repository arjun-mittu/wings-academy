from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from .models import Blog,comment
from .forms import cmtform
def home(request):
    return render(request,"home.html")

#def all_blogs(request):
#   return render(request,"all_blogs.html")
class all_blogs(ListView):
    model=Blog
    template_name='all_blogs.html'
    context_object_name='blogs'
    ordering=['-date_posted']
    paginate_by=6
    def get_queryset(self):
        result= super(all_blogs,self).get_queryset()
        query=self.request.GET.get('search')
        if query:
            postresult = Blog.objects.filter(title__contains=query)
            result = postresult
        else:
            result = Blog.objects.order_by('-date_posted')
        return result

def Blogdetailview(request,pk):
    template_name='single-blog-page.html'
    post=get_object_or_404(Blog,id=pk)
    comments=comment.objects.filter(blog=post).order_by('-created_on')
    if request.method=='POST':
        comment_form=cmtform(request.POST or None)
        try:
            if comment_form.is_valid():
                user=request.user
                body=comment_form.cleaned_data.get('body')
                comment_form1=comment.objects.create(
                    blog=post,
                    by=user,
                    body=body
                )
        except ObjectDoesNotExist:
            messages.error(self.request,"fill correctly")
    else:
        comment_form=cmtform()
    return render(request,template_name,{'post':post,'comments':comments,'comment_form':cmtform})

def my_profile(request):
    return render(request,"profile.html")