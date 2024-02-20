from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.WeblogCategroy)
admin.site.register(models.Weblog)
admin.site.register(models.WeblogComment)
admin.site.register(models.IpModel)
admin.site.register(models.WeblogVideo)
admin.site.register(models.WeblogVideoComment)
