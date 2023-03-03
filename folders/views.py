from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import Folder2Serializer
from .models import Folder2
from rest_framework.views import APIView
# Create your views here.

#폴더 정보 등록 api
class FolderView(APIView):
    def post(self, request):
        serializer = Folder2Serializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save(user=request.user)
            serializer.save() 
            return Response({"message : ok"}, status=status.HTTP_200_OK)
        return Response({"message : fail"}, status=status.HTTP_409_CONFLICT)
        
    def get(self, request):
        tmp = Folder2.objects.filter(user_id = request.user.id)
        res = []
        i=0
        n=len(tmp)
        while i < n:
            res.append(tmp[i].folder_name)
            i+=1
        return Response(res, status=status.HTTP_200_OK)