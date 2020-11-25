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