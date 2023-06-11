import json
import logging
from django.db import IntegrityError
from django.forms import ValidationError
from accounts.models import CustomUser
from music.models import Artist, History
from .util import *

logger = logging.getLogger(__name__)


class HistoryImporter:
    def execute(self):
        created = 0
        failed = 0
        with open("endsong_0.json", encoding="utf-8") as spotify_json:
            spotify_data = json.loads(spotify_json.read())

            for history_data in spotify_data:
                try:
                    logger.info(
                        f"importing {history_data['master_metadata_album_artist_name']} - {history_data['master_metadata_track_name']}"
                    )
                    History.create(**history_data)
                    created += 1
                except (
                    TypeError,
                    AttributeError,
                    ValidationError,
                    IntegrityError,
                ) as e:
                    logger.info(
                        f"Error Exception: {e} - {history_data['master_metadata_album_artist_name']} - {history_data['master_metadata_track_name']}"
                    )
                    failed += 1
            logger.info(f"created: {created}, failed: {failed}")


class RecentHistoryImporter:
    def execute(self, username):
        user = CustomUser.objects.get(username=username)
        history = execute_spotify_api_request(user, "player/recently-played?limit=50")
        for track in history:
            print(
                f"album name {track['track']['album']['name']}"
            )  # TODO: hit api to grab album details
            print(f"track name {track['track']['name']}")
            for artist in track["track"]["artists"]:
                print(f"artist name {artist['name']}")
                Artist.objects.get_or_create(
                    name=artist["name"]
                )  # TODO: update the artist model to accept a full api request
            print(f"played at {track['played_at']}")
