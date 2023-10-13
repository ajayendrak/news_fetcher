from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from news.models import *
from user.serializers import *

class UserKeywordsSerializers(serializers.ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = UserKeywords
        fields = (
            "user",
            'keyword',
            'created_at',
        )

    def get_user(self,obj):
        try:
            return UserSerializers(obj.user).data
        except Exception as e:
            return ""