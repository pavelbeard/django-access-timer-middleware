from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.AccessTime)
class Admin(admin.ModelAdmin):
    pass
