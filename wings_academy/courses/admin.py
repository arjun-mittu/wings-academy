from django.contrib import admin
from .models import course,lesson
# Register your models here.
class lessonsadmin(admin.ModelAdmin):
    list_display=('course','title')
admin.site.register(course)
admin.site.register(lesson,lessonsadmin)
