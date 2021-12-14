from django.contrib import admin

from .models import *

admin.site.register(Dentist)
admin.site.register(Coordinate)
admin.site.register(Openinghours)