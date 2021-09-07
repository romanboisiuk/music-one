from django.contrib import admin

from .models import *


class StoryHashtagAdmin(admin.ModelAdmin):
    pass


admin.site.register(StoryHashtag, StoryHashtagAdmin)


class IgtvHashtagAdmin(admin.ModelAdmin):
    pass


admin.site.register(IgtvHashtag, IgtvHashtagAdmin)


class StoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Story, StoryAdmin)


class IgtvAdmin(admin.ModelAdmin):
    pass


admin.site.register(Igtv, IgtvAdmin)


class HighlightAdmin(admin.ModelAdmin):
    pass


admin.site.register(Highlight, HighlightAdmin)
