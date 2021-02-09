from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import NoteSerializer
from .models import Note

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        queryset = Note.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title='title')
        return queryset