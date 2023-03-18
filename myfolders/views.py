from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import FolderSerializer
from .models import Folder
from rest_framework.views import APIView
# Create your views here.

#폴더 정보 등록 api
class FolderView(APIView):
    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        serializer.fields['sender'].required = False
        serializer.fields['keyword'].required = False
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            serializer.save()
            return Response({"message : ok"}, status=status.HTTP_200_OK)
        return Response({"message : fail"}, status=status.HTTP_409_CONFLICT)
        
    def get(self, request):
        tmp = Folder.objects.filter(user_id = request.user.id)
        
        serializer = FolderSerializer(tmp, many=True)
        last = []
        tete = {"user":request.user.id, "folder_name":"전체"}
        last.append(tete)
        last.append(serializer.data)
        return Response(last)
        '''
        res = []
        i=0
        n=len(tmp)
        while i < n:
            res.append(tmp[i].folder_name)
            i+=1
        return Response(res, status=status.HTTP_200_OK)
        '''



class CusFolderView(APIView):
    def get(self, request, pk):
        tmp = Folder.objects.filter(user_id=request.user.id)
        res = tmp[pk]
        serializer = FolderSerializer(res)

        return Response(serializer.data)

    def delete(self, request, pk):
        tmp = Folder.objects.filter(user_id=request.user.id)
        res = tmp[pk]
        res.delete()
        return Response("message : delete is success", status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        tmp = Folder.objects.filter(user_id=request.user.id)
        res = tmp[pk]
        serializer = FolderSerializer(res, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("message : put error", status=status.HTTP_409_CONFLICT)
    

class IdFolderView(APIView):
    def get(self, request, pk, format=None):
        tmp = Folder.objects.get(pk=pk)
        serializer = FolderSerializer(tmp)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        tmp = Folder.objects.get(pk=pk)
        tmp.delete()
        return Response("message : delete success", status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        tmp = Folder.objects.get(pk=pk)
        serializer = FolderSerializer(tmp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("message : put error", status=status.HTTP_409_CONFLICT)
        

