from django.contrib import admin
from modelapp3.models import EmpRegistration
# Register your models here.

class EmpDetails(admin.ModelAdmin):
    list_display=['eid','ename','esal']
admin.site.register(EmpRegistration,EmpDetails)
