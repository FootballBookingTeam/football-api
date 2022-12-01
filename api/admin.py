from django.contrib import admin
from .models import User, Turf, Image, Schedule
# Register your models here.
admin.site.register(User)
admin.site.register(Turf)
admin.site.register(Image)
admin.site.register(Schedule)
