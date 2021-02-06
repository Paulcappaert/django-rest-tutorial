from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note

@api_view()
def notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(data=serializer.data)

@api_view()
def note(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note)
    return Response(data=serializer.data)