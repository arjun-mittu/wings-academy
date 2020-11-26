from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import home,all_blogs,Blogdetailview,my_profile,pay_home,payment,response
app_name="core"
urlpatterns = [
    path('',home,name="home"),
    path('blogs/',all_blogs.as_view(),name="all_blogs"),
    path('blogs/<int:pk>',Blogdetailview,name='post-detail'),
    path('profile/',my_profile,name='profile'),
    path('pay_home/',pay_home,name='pay_home'),
    path('payment/',payment,name='paymeny'),
    path('response/',response,name='response'),
]
