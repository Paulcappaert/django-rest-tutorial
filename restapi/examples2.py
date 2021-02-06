import django
from django.conf import settings
from restapi import settings
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'restapi.settings'

django.setup()

from notes.serializers import NoteSerializer
from notes.models import Note

## serialize a saved and not saved note
# note = Note(
#     title='title',
#     content='content',
# )

# note.save()

# serializer = NoteSerializer(note)

# print(serializer.data)

## Create a new note
# data = {
#     'title': 'title',
#     'content': 'content'
# }

# serializer = NoteSerializer(data=data)

# print(serializer.is_valid())

# print(serializer.validated_data)

# instance = serializer.save()

# print(instance.id)

## update a note
# note = Note.objects.create(
#     title = 'new note', content='some content'
# )

# serializer = NoteSerializer(instance=note, data = {'content': 'new content', 'title': 'new note'})

# print(serializer.is_valid())
# print(serializer.validated_data)

# serializer.save()

# print(note.content)

