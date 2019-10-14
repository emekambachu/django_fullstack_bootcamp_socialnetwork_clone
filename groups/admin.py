from django.contrib import admin
from . import models

# Register your models here.

# connecting GroupMember class from models to admin
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)