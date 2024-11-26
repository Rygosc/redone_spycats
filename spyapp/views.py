from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SpyCatSerializer
from django.shortcuts import get_object_or_404
from .models import SpyCat


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
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)