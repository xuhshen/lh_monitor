from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import *
from rest_framework.exceptions import ErrorDetail, ValidationError

class IndexSerializer(serializers.ModelSerializer):
    holdlist = serializers.JSONField(source="getholdlist")
    lastinfo = serializers.JSONField(source="getlastinfo")
    accountinfo = serializers.JSONField(source="getlatestinfo")
    yearinfo = serializers.JSONField(source="getyearstartinfo")
    yesterdayinfo = serializers.JSONField(source="getyesterdayinfo")
    moninfo = serializers.JSONField(source="getmonstartinfo")
    holdnum = serializers.FloatField(source="getholdnum")
    project = serializers.CharField(source="project.name")
    
    class Meta:
        model = Account
        fields = "__all__" 