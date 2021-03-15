from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Career)
admin.site.register(Comparison)
admin.site.register(Result)
admin.site.register(Chart)