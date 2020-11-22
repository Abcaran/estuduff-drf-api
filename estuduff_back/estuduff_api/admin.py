from django.contrib import admin

from estuduff_api import models

# Register your models here.
admin.site.register(models.Modality)
admin.site.register(models.Degree)
admin.site.register(models.Program)
admin.site.register(models.StudyProfile)
admin.site.register(models.StudyPlaceType)
admin.site.register(models.Campus)
admin.site.register(models.Building)
admin.site.register(models.StudyPlace)
admin.site.register(models.User)
