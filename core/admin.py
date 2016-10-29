from django.contrib import admin
from .models import Box, BoxLog

class BoxAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']

class BoxLogAdmin(admin.ModelAdmin):
	list_display = ['datetime']
	search_fields = ['datetime']

admin.site.register(Box, BoxAdmin)
admin.site.register(BoxLog, BoxLogAdmin)