from django.db import models

from accounts.models import CustomUser


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.album_name)


class Track(models.Model):
    track_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.track_name)


class History(models.Model):
    ts = models.DateTimeField(unique=True)
    username = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)
    ms_played = models.IntegerField()
    conn_country = models.CharField(max_length=30)
    ip_addr_decrypted = models.CharField(max_length=30)
    user_agent_decrypted = models.CharField(max_length=30, null=True)
    master_metadata_track_name = models.CharField(max_length=100)
    master_metadata_album_artist_name = models.CharField(max_length=100)
    master_metadata_album_album_name = models.CharField(max_length=100)
    spotify_track_uri = models.CharField(max_length=30, null=True)
    episode_name = models.CharField(max_length=30, null=True)
    spotify_episode_uri = models.CharField(max_length=30, null=True)
    reason_start = models.CharField(max_length=30)
    reason_end = models.CharField(max_length=30)
    shuffle = models.BooleanField(default=False)
    skipped = models.CharField(max_length=30, null=True)
    offline = models.BooleanField(default=False)
    offline_timestamp = models.CharField(max_length=30)
    incognito_mode = models.BooleanField(default=False)

    @classmethod
    def create(cls, **kwargs):
        song = cls.objects.create(
            ts=kwargs["ts"],
            username=kwargs["username"],
            platform=kwargs["platform"],
            ms_played=kwargs["ms_played"],
            conn_country=kwargs["conn_country"],
            ip_addr_decrypted=kwargs["ip_addr_decrypted"],
            user_agent_decrypted=kwargs["user_agent_decrypted"],
            master_metadata_track_name=kwargs["master_metadata_track_name"],
            master_metadata_album_artist_name=kwargs[
                "master_metadata_album_artist_name"
            ],
            master_metadata_album_album_name=kwargs["master_metadata_album_album_name"],
            spotify_track_uri=kwargs["spotify_track_uri"],
            episode_name=kwargs["episode_name"],
            spotify_episode_uri=kwargs["spotify_episode_uri"],
            reason_start=kwargs["reason_start"],
            reason_end=kwargs["reason_end"],
            shuffle=kwargs["shuffle"],
            skipped=kwargs["skipped"],
            offline=kwargs["offline"],
            offline_timestamp=kwargs["offline_timestamp"],
            incognito_mode=kwargs["incognito_mode"],
        )
        Artist.objects.get_or_create(name=kwargs["master_metadata_album_artist_name"])
        Track.objects.get_or_create(
            track_name=kwargs["master_metadata_track_name"],
            album_name=kwargs["master_metadata_album_album_name"],
            artist_name=kwargs["master_metadata_album_artist_name"],
        )
        Album.objects.get_or_create(
            album_name=kwargs["master_metadata_album_album_name"],
            artist_name=kwargs["master_metadata_album_artist_name"],
        )

        return song


class SpotifyToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)
