from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from registration.models import User, Host, Visitor

admin.site.register(User, UserAdmin)
admin.site.register(Host)
admin.site.register(Visitor)