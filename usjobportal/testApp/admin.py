from django.contrib import admin
from testApp.models import *
# Register your models here.

class hydAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_number']

class blrAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_number']

class bbsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone_number']


admin.site.register(hydjobs,hydAdmin)
admin.site.register(blrjobs,blrAdmin)
admin.site.register(bbsjobs,bbsAdmin)
