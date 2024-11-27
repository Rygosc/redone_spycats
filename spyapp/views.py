from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer
from django.shortcuts import get_object_or_404
from .models import SpyCat, Mission, Target


class SpyCatDetailView(APIView):
    def get(self, request, pk=None):
        if pk:
            spycat = get_object_or_404(SpyCat, pk=pk)
            serializer = SpyCatSerializer(spycat)
        else:
            spycats = SpyCat.objects.all()
            serializer = SpyCatSerializer(spycats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpyCatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        spycat = get_object_or_404(SpyCat, pk=pk)
        serializer = SpyCatSerializer(spycat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        spycat = get_object_or_404(SpyCat, pk=pk)
        spycat.delete()
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class MissionView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                mission = Mission.objects.get(pk=pk)
                serializer = MissionSerializer(mission)
                return Response(serializer.data)
            except Mission.DoesNotExist:
                return Response({"Error": "Mission not found"}, status=status.HTTP_404_NOT_FOUND)
        mission = Mission.objects.all()
        serializer = MissionSerializer(mission, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            return Response({"Error": "Mission not found"})
        serializer = MissionSerializer(mission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
            if mission.cat:
                return Response({"Error": "Cannot delete a mission assigned to a cat"}, status=status.HTTP_400_BAD_REQUEST)
            mission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Mission.DoesNotExist:
            return Response({"Error": "Mission not found"})


class TargetsView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                target = Target.objects.get(pk=pk)
                serializer = TargetSerializer(target)
                return Response(serializer.data)
            except Target.DoesNotExist:
                return Response({"Error": "Target not found"}, status=status.HTTP_404_NOT_FOUND)
        target = Target.objects.all()
        serializer = TargetSerializer(target, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            target = Target.objects.get(pk=pk)
        except Target.DoesNotExist:
            return Response({"Error": "target not found"})
        serializer = TargetSerializer(target, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
