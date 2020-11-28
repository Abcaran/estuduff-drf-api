from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import User

from .models import *


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = '__all__'
        read_only_fields = ('id',)


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'
        read_only_fields = ('id',)


class ProgramSerializer(serializers.ModelSerializer):
    modality = serializers.PrimaryKeyRelatedField(
        queryset=Modality.objects.all()
    )
    degree = serializers.PrimaryKeyRelatedField(
        queryset=Degree.objects.all()
    )

    class Meta:
        model = Program
        fields = '__all__'
        read_only_fields = ('id',)


class StudyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProfile
        fields = '__all__'
        read_only_fields = ('id',)


class StudyPlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlaceType
        fields = '__all__'
        read_only_fields = ('id',)


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'
        read_only_fields = ('id',)


class BuildingSerializer(serializers.ModelSerializer):
    campus = serializers.PrimaryKeyRelatedField(queryset=Campus.objects.all())

    class Meta:
        model = Building
        fields = '__all__'
        read_only_fields = ('id',)


class StudyPlaceSerializer(serializers.ModelSerializer):
    building = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all()
    )
    studyPlaceType = serializers.PrimaryKeyRelatedField(
        queryset=StudyPlaceType.objects.all()
    )
    studyProfile = serializers.PrimaryKeyRelatedField(
        many=True, queryset=StudyProfile.objects.all()
    )

    class Meta:
        model = StudyPlace
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    program = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Program.objects.all()
    )
    studyProfile = serializers.PrimaryKeyRelatedField(
        queryset=StudyProfile.objects.all()
    )

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)
