from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from robots.models import Manufacturer, Robot, RobotCategory
from robots.serializers import (ManufacturerSerializer,
                                RobotCategorySerializer, RobotSerializer)


def home(request):
    return render(request, 'home.html')


def manu(request):
    if request.method == 'POST':
        # Perform successful submit/post logic here
        return redirect('thanks')
    else:
        return render(request, 'manu.html')


def manudetail(request):
    return render(request, 'manudetail.html')


def robocat(request):
    return render(request, 'robocat.html')


def thanks(request):
    # print("inside thanks function")
    return render(request, 'thanks.html')


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'robot-categories': reverse(RobotCategoryList.name, request=request),
            'manufacturers': reverse(ManufacturerList.name, request=request),
            'robots': reverse(RobotList.name, request=request)
        })


class RobotCategoryList(generics.ListCreateAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer
    name = 'robotcategory-list'


class RobotCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer
    name = 'robotcategory-detail'


class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    name = 'manufacturer-list'


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    name = 'manufacturer-detail'


class RobotList(generics.ListCreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'robot-list'


class RobotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    name = 'robot-detail'
