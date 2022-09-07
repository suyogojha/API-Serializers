from rest_framework import viewsets
from rest_framework.response import Response
from home.models import Students, Modules, Teacher
from .serializer import StudentsSerializer, ModulesSerializer, TeacherSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        student = Students.objects.all()
        return student

    def create(self, request, *args, **kwargs):
        data = request.data
        for module in data["modules"]:
            module_obj = Modules.objects.get(module_name=module["module_name"])
        serializer = StudentsSerializer(module_obj)
        return Response(serializer.data)


class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer

    def get_queryset(self):
        module = Modules.objects.all()
        return module



class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        module = Teacher.objects.all()
        return module