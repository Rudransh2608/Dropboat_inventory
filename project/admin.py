from django.contrib import admin
from .models import Project

admin.site.site_header='Dropboat'
admin.site.register(Project)
