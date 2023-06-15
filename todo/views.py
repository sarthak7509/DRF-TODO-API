from django.shortcuts import render
from rest_framework import viewsets
from core.models import TODO
from .serializer import TODOserializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TODOViewSet(viewsets.ModelViewSet):
    serializer_class = TODOserializer
    permission_classes = [IsAuthenticated]
    queryset = TODO.objects.all()
    def get_queryset(self):
        query_set = self.queryset
        return query_set.filter(user=self.request.user).order_by('-id')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)