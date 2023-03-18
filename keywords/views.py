from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import KeywordSerializer
from .models import KeywordUser

# Create your views here.

class KeywordView(APIView):
    def post(self, request):
        serializer = KeywordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message : keyword post fail"}, status=status.HTTP_409_CONFLICT)
    
    def get(self, request):
        tmp = KeywordUser.objects.filter(user_id = request.user.id)
        serializer = KeywordSerializer(tmp, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class DeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            tmp = KeywordUser.objects.get(pk=pk)
            tmp.delete()
            return Response({"message : delete success"}, status=status.HTTP_200_OK)
        except:
            return Response({"message : delete id not found"}, status=status.HTTP_409_CONFLICT)
            
        
        