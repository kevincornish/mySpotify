from django.contrib import admin

from .models import History, Artist, Album, Track


class HistoryAdmin(admin.ModelAdmin):
    list_display = [
        "master_metadata_track_name",
        "master_metadata_album_artist_name",
        "master_metadata_album_album_name",
        "ts",
    ]


class ArtistAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "album_name",
        "artist_name",
    ]


class TrackAdmin(admin.ModelAdmin):
    list_display = [
        "track_name",
        "album_name",
        "artist_name",
    ]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Track, TrackAdmin)
