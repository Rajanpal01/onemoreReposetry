from django.contrib import admin
from .models import Project_details,Projects_ideas,Form_data
from .models import PPT, Documentation


# Register your models here.
admin.site.register(Project_details)
admin.site.register(Projects_ideas)
admin.site.register(Form_data)
admin.site.register(PPT)
admin.site.register(Documentation)
