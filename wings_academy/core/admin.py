from django.contrib import admin
from .models import Blog,comment,paid
# Register your models here.
class paidadmin(admin.ModelAdmin):
    list_display=('user','type')
admin.site.register(paid,paidadmin)
admin.site.register(Blog)
admin.site.register(comment)