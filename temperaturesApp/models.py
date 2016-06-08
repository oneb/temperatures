from django.db import models
from django.utils import timezone
from django.conf import settings
import decimal

class TmpReading(models.Model):
    tmp = models.DecimalField(max_digits=settings.TMP_MAX_DIGITS, 
        decimal_places=settings.TMP_DECIMAL_PLACES)
    timestamp = models.DateTimeField(default=timezone.now, blank=True, db_index=True)
    
    def __str__(self):
        return '{0} at {1}'.format(str(self.tmp), str(self.timestamp))

