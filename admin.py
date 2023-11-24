from django.contrib import admin

# Register your models here.
from .models import user_login, user_details, police_station_master, station_user

from.models import user_login
from.models import user_details


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(police_station_master)
admin.site.register(station_user)

