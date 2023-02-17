from django.contrib import admin
from form_test.models import Restaurant, Food

class RestaurantAdmin(admin.ModelAdmin): # list_display search_fields為固定用法
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name',) 

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food)