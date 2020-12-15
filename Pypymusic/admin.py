from django.contrib import admin
import time

# Register your models here.
from Pypymusic.models import Album, Song, Artist

class PypymusicAdministration(admin.AdminSite):
  admin.site.site_header = "Pypymusic Admin"
  admin.site.site_title = "Pypymusic Admin Portal"
  admin.site.index_title = "Welcome to Pypymusic Researcher Portal"

admin_site = PypymusicAdministration(name='admin')

@admin.register(Album, site = admin_site)
class AlbumAdmin(admin.ModelAdmin):
  readonly_fields = ('release_date', )
  list_display = ('name', 'artist', 'release_date')

  autocomplete_fields = ('artist', )

# admin.site.register(Album, AlbumAdmin)

@admin.register(Song, site = admin_site)
class SongAdmin(admin.ModelAdmin):
  save_on_top = True
  list_display = ('name', 'album', 'duration_human_readable')
  list_filter = ('name', 'album__artist__last_name')

  def duration_human_readable(self, obj):
    return time.strftime('%M:%S', time.gmtime(obj.duration))
  duration_human_readable.short_description = "Duration"
  duration_human_readable.admin_order_field = 'duration'



@admin.register(Artist, site = admin_site)
class ArtistAdmin(admin.ModelAdmin):
  save_on_top = True
  list_display = ('full_name', 'join_date', 'published')
  list_filter = ('published', )


  search_fields = ('first_name', 'last_name', 'join_date', 'published')