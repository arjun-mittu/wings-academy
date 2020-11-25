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
from .models import course
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
    if check_paid.type=="paid":
        return HttpResponse('paid')
    elif check_paid.type=="free" and post.type=="paid":
        return render(request,"member_required.html")
    elif check_paid.type=="free" and post.type=="free":
        return HttpResponse('free + free')
    

@login_required
def membership_required(request,pk):
    return render(request,'member_required.html')