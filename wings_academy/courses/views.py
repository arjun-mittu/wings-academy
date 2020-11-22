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

def home(request):
    return HttpResponse('hello')