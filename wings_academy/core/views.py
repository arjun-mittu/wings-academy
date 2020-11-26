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
from . import Checksum
from core.utils import VerifyPaytmResponse
def home(request):
    return render(request,"home.html")

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



def pay_home(request):
    return HttpResponse("<html><a href='http://localhost:8000/payment'>PayNow</html>")

def payment(request):
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    data_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        #'MOBILE_NO': '7405505665',
        #'EMAIL': 'dhaval.savalia6@gmail.com',
        'CUST_ID': '123123',
        'ORDER_ID':order_id,
        'TXN_AMOUNT': bill_amount,
    } # This data should ideally come from database
    data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)
    context = {
        'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
        'comany_name': settings.PAYTM_COMPANY_NAME,
        'data_dict': data_dict
    }
    return render(request, 'payments/payment.html', context)


@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Successful</h1><center>", status=200)
    else:
        # check what happened; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)