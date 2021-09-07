from django.contrib import admin
from main.models import *


class MusicOneUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(MusicOneUser, MusicOneUserAdmin)
