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
from .models import course,lesson
from core.models import paid
class home(ListView):
    model=course
    template_name='all_courses.html'
    context_object_name='course'
    ordering=['-created_on']
    paginate_by=6
    def get_queryset(self):
        result= super(home,self).get_queryset()
        query=self.request.GET.get('search')
        if query:
            postresult = course.objects.filter(title__contains=query)
            result = postresult
        else:
            result = course.objects.order_by('-created_on')
        return result

@login_required
def course_detail_view(request,pk):
    user_logged=request.user
    check_paid=paid.objects.filter(user=user_logged)[0]
    post=get_object_or_404(course,id=pk)
    cl=lesson.objects.filter(course=post).order_by('video_number')
    if check_paid.type=="paid":
        context={
            "post":post,
            "cl":cl
        }
        return render(request,"course_detail.html",context)
    elif check_paid.type=="free" and post.type=="paid":
        return render(request,"member_required.html")
    elif check_paid.type=="free" and post.type=="free":
        context={
            "post":post,
            "cl":cl
        }
        return render(request,"course_detail.html",context)

@login_required
def video_detail_view(request,pk,*args, **kwargs):
    user_logged=request.user
    if request.method=='GET':
        video_id=kwargs.get("video_id")
        check_paid=paid.objects.filter(user=user_logged)[0]
        post=get_object_or_404(course,id=pk)
        cl=lesson.objects.filter(course=post).order_by('video_number')
        now_lesson=lesson.objects.filter(course=post)
        nl=now_lesson.filter(id=video_id)[0]
        if check_paid.type=="paid":
            context={
                "post":post,
                "cl":cl,
                "nl":nl
            }
            return render(request,"course_video.html",context)
        elif check_paid.type=="free" and post.type=="paid":
            return render(request,"member_required.html")
        elif check_paid.type=="free" and post.type=="free":
            context={
                "post":post,
                "cl":cl,
                "nl":nl
            }
            return render(request,"course_video.html",context)
    

