from django.core.management import BaseCommand
from music.importer import RecentHistoryImporter


class Command(BaseCommand):
    help = "import recent spotify listen history to specific user"
    def add_arguments(self, parser):
        parser.add_argument('username',  type=str)

    def handle(self, *args, **options):
        RecentHistoryImporter.execute(self, options['username'])
