from django.contrib import admin
from .models import Profile , Appointment 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','address','number_phone','doctor','specialist_doctor' )
    list_filter = ('type_doctors'  , 'address' ,'price')
    search_fields = ('name','address')
admin.site.register(Profile , ProfileAdmin)
admin.site.register(Appointment)