from django.contrib import admin
from .models import Device, Location

# Register your models here.

# Creating access to classes in the admin portal
# Admin portal is only accessible to superusers
admin.site.register(Device)
admin.site.register(Location)
