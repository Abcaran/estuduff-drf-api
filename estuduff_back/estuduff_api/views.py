from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework import status


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

    def _params_to_ints(self, qs):
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        studyPlaceType = self.request.query_params.get('studyPlaceType')
        studyProfile = self.request.query_params.get('studyProfile')
        queryset = self.queryset

        if studyPlaceType:
            study_place_type = self._params_to_ints(studyPlaceType)
            queryset = queryset.filter(studyPlaceType__id__in=study_place_type)

        if studyProfile:
            study_profile = self._params_to_ints(studyProfile)
            queryset = queryset.filter(studyProfile__id__in=study_profile)

        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email and password:
            is_user = User.objects.filter(
                email=email, password=password).exists()

            if is_user:
                return Response(status.HTTP_200_OK)

            return Response(status.HTTP_401_UNAUTHORIZED)

        return Response(status.HTTP_400_BAD_REQUEST)
