from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Tour)
admin.site.register(DayTrips)
admin.site.register(Order)
