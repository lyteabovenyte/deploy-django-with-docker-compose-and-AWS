"""
django command to wait for the database to be available
"""

import time
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''django command to wait for database'''

    def handle(self, *args, **options):
        '''Entrypoint for command'''

        self.stdout.write('waiting for database...')
        db_up = False
        while db_up == False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError, OperationalError):
                self.stdout.write('database is not available, wait for 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database is available!'))
