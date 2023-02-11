from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from .serializers import FilterSerializer
from .models import Filter

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)