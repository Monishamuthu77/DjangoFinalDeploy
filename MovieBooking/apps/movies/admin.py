from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Listing
from django.contrib import admin
from embed_video.admin import AdminVideoMixin


class MovieAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('id', 'screen', 'movie_name', 'branch', 'is_published', 'list_date')
    list_display_links = ('id','movie_name')
    list_filter = ('screen', 'movie_name', )
    search_fields = ('movie_name','branch', )
    list_editable = ('is_published', )

admin.site.register(Listing, MovieAdmin)


