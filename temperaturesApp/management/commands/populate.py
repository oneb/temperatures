from django.core.management.base import BaseCommand, CommandError
from temperaturesApp.models import TmpReading
from django.utils import timezone
import datetime
import random, decimal


def populate(count):

    now = timezone.now()
    accum = []

    for t in range(count, 0, -1):
        timestamp = now - datetime.timedelta(days=7, seconds=t*2)

        tmp = decimal.Decimal(random.random() * 100 - 50)
        tmp = round(tmp, random.randint(0,4))
        tmp = str(tmp)

        accum.append(TmpReading(tmp=tmp, timestamp=timestamp))

        if t % 512 == 0 or t == 1:
            TmpReading.objects.bulk_create(accum)
            accum = []
            print('.', end='', flush=True)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        print('populating with {0} readings'.format(count))
        populate(count)
        print('done')



