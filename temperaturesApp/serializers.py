from django.conf import settings 
from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError
from . import models


class AutoRoundingDecimalField(fields.DecimalField):

    def validate_precision(self, value):
        value = round(value, 2)
        return super(AutoRoundingDecimalField, self).validate_precision(value)


class TmpReadingSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    tmp = AutoRoundingDecimalField(decimal_places=settings.TMP_DECIMAL_PLACES,
        max_digits=settings.TMP_MAX_DIGITS)
    class Meta:
        model = models.TmpReading
        fields = ('tmp', 'timestamp', 'id')
