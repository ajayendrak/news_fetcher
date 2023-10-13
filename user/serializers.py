from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from user.models import *
from rest_framework.serializers import SerializerMethodField
import json


class UserSignUpSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )

class UserLoginSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = (
            "email",
            'password',
        )

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )