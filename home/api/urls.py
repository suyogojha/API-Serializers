from django.urls import path,  include
from .views import StudentsViewSet, ModulesViewSet, TeacherViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("student", StudentsViewSet, basename="student")
router.register("module", ModulesViewSet, basename="module")
router.register("teacher", TeacherViewSet, basename="teacher")


urlpatterns = [
    path('', include(router.urls))
]