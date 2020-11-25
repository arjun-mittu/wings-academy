from django.contrib import admin
from .models import course,lessons
# Register your models here.
class lessonsadmin(admin.ModelAdmin):
    list_display=('course','title')
admin.site.register(course)
admin.site.register(lessons,lessonsadmin)
