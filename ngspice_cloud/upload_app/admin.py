from django.contrib import admin
from .models import Task, spiceFile

# Register your models here.
admin.site.register(Task)
admin.site.register(spiceFile)