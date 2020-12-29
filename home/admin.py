from django.contrib import admin

# Register your models here.
from .models import task

admin.site.register(task)