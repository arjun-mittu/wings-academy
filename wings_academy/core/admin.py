from django.contrib import admin
from .models import Blog,comment,paid,contact
# Register your models here.
class paidadmin(admin.ModelAdmin):
    list_display=('user','type')

class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phoneno','msg')

admin.site.register(contact,contactadmin)
admin.site.register(paid,paidadmin)
admin.site.register(Blog)
admin.site.register(comment)