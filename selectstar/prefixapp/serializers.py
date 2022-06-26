from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PrefixSerializer(serializers.Serializer):
    data_li = serializers.ListField(child=serializers.CharField(min_length=1, max_length=100))
