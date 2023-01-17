from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .serializers import BoardSerializer, KeywordSerializer, FilterSerializer
from .models import Board, Keyword, Filter
'''
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly] 원래 이거임
    permission_classes = [permissions.IsAuthenticated]
    if permission_classes==False:
        Response({"message": "로그인된 사용자가 아닙니다"}, status=status.HTTP_409_CONFLICT)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
'''

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
