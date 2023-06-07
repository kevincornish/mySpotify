import json
import logging
from django.db import IntegrityError

from django.forms import ValidationError
from music.models import History

logger = logging.getLogger(__name__)


class HistoryImporter:
    def import_history(self):
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
