from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin
# Register your models here.

from models import Flat, FlatPhoto, FlatFeatures, Feedback


class FlatAdmin(MCEFilebrowserAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Flat, FlatAdmin)
admin.site.register(Feedback)
admin.site.register(FlatPhoto)
admin.site.register(FlatFeatures)
