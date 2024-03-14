from django.contrib import admin
from .models import Query,Feedback,User,Employee_Type,Employee,Offers_Scheme


#costomised django admin panel
class User_Admin(admin.ModelAdmin):
    list_display=('name','email','phone')
    

class Employee_Admin(admin.ModelAdmin):
    list_display=( 'employee_type','name','phone')
    # list_filter=['designation']   

# class Student_Admin(admin.ModelAdmin):
#     list_display=('name','email','phone','gender')     



# Register your models here.
admin.site.register(Query)
admin.site.register(Feedback)
admin.site.register(User,User_Admin)
admin.site.register(Offers_Scheme)
admin.site.register(Employee_Type)
admin.site.register(Employee,Employee_Admin)

#admin updation
admin.site.site_header="SHome Solution Administration"
admin.site.site_title="SHome Admin Dashboard"
admin.site.index_title="CompanyAdmin"

