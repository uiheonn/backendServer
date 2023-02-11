from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

<<<<<<< HEAD
from .serializers import KeywordSerializer, BoardSerializer
from .models import Keyword, Board
=======
from .serializers import BoardSerializer, KeywordSerializer, FilterSerializer
from .models import Board, Keyword, Filter
>>>>>>> 0327693067534ab5ff41e7507bb778fe7c46cc9f
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
<<<<<<< HEAD

=======
        
>>>>>>> 0327693067534ab5ff41e7507bb778fe7c46cc9f
class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
<<<<<<< HEAD
'''
class FilteringViewSet(viewsets.ModelViewSet):
    queryset = Filtering.objects.all()
    serializer_class = FilteringSerializer
=======

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
>>>>>>> 0327693067534ab5ff41e7507bb778fe7c46cc9f
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
<<<<<<< HEAD

'''
=======
>>>>>>> 0327693067534ab5ff41e7507bb778fe7c46cc9f
