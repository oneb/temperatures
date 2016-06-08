from django.core.management.base import BaseCommand
from temperaturesApp.models import TmpReading
from django.utils import timezone
import datetime
import random, decimal

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('deleting all stored temperature readings')
        TmpReading.objects.all().delete()
        print('done')



