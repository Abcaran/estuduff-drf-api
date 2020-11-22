from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'modality', views.ModalityViewSet)
router.register(r'degree', views.DegreeViewSet)
router.register(r'program', views.ProgramViewSet)
router.register(r'studyprofile', views.StudyProfileViewSet)
router.register(r'studyplacetype', views.StudyPlaceTypeViewSet)
router.register(r'campus', views.CampusViewSet)
router.register(r'building', views.BuildingViewSet)
router.register(r'studyplace', views.StudyPlaceViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
         namespace='rest_framework'
         )
         )
]
