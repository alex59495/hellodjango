from django.contrib import admin
import time

# Register your models here.
from appone.models import Album, Song

class AlbumAdmin(admin.ModelAdmin):
  # fields = ('name',  )
  readonly_fields = ('release_date', )
  search_fields = ["name", 'artist_name']

  list_display = ('name', 'artist_name', 'release_date', )
  list_editable = ('artist_name', )
  list_filter = ('artist_name', )
admin.site.register(Album, AlbumAdmin)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
  save_on_top = True
  exclude = ('lyrics', )
  autocomplete_fields = ('album', )

  list_display = ('name',
                  'album', 
                  'duration_human_readable'
                  )

  search_fields = ('album__name', 'name', 'album__artist_name')

  list_filter = ('album__name', 'album__artist_name')

  def duration_human_readable(self, obj):
    return time.strftime('%M:%S', time.gmtime(obj.duration))
  duration_human_readable.short_description = 'Duration'
  duration_human_readable.admin_order_field = 'duration'
