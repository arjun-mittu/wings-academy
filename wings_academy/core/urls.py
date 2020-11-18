from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import home,all_blogs
app_name="core"
urlpatterns = [
    path('',home,name="home"),
    path('blogs/',all_blogs.as_view(),name="all_blogs"),
]
