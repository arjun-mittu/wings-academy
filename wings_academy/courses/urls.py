from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import home,course_detail_view
app_name="courses"
urlpatterns = [
    path('',home.as_view(),name="home"),
    path('<int:pk>',course_detail_view,name="course_detail"),
]
