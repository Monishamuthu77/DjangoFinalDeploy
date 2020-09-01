from django.contrib import admin
from .models import Screen

class TeatresAdmin(admin.ModelAdmin):
    list_display = ('id', 'theatre_name', 'screen_name')
    list_display_links = ('id', 'theatre_name')
    list_filter = ('theatre_name', )
    search_fields = ('theatre_name', )
    list_editable = ('is_mvp', )

admin.site.register(Screen)
