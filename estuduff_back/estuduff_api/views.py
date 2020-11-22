from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all().order_by('name')
    serializer_class = ModalitySerializer


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all().order_by('name')
    serializer_class = DegreeSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all().order_by('name')
    serializer_class = ProgramSerializer


class StudyProfileViewSet(viewsets.ModelViewSet):
    queryset = StudyProfile.objects.all().order_by('name')
    serializer_class = StudyProfileSerializer


class StudyPlaceTypeViewSet(viewsets.ModelViewSet):
    queryset = StudyPlaceType.objects.all().order_by('name')
    serializer_class = StudyPlaceTypeSerializer


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all().order_by('name')
    serializer_class = CampusSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all().order_by('name')
    serializer_class = BuildingSerializer


class StudyPlaceViewSet(viewsets.ModelViewSet):
    queryset = StudyPlace.objects.all().order_by('name')
    serializer_class = StudyPlaceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer
