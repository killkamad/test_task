from django.contrib import admin
from .models import UserProfile, Record, Status, Template


admin.site.register(UserProfile)
admin.site.register(Record)
admin.site.register(Status)
admin.site.register(Template)
