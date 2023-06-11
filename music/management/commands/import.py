from django.core.management import BaseCommand
from music.importer import HistoryImporter


class Command(BaseCommand):
    help = "import spotify history"

    def handle(self, *args, **options):
        HistoryImporter.execute(self)
