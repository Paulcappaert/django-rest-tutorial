from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import NoteSerializer
from .models import Note

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(data=serializer.data)
    else:
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(data=serializer.data)
    else:
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)