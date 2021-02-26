from rest_framework import serializers
from . import models


class TmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TmpModel