from django.contrib import admin
from flag.models import FlaggedContent, FlagInstance

admin.site.register(FlaggedContent)
admin.site.register(FlagInstance)
