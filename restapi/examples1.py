import django
from django.conf import settings
from restapi import settings
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'restapi.settings'

django.setup()

from notes.models import Note

note = Note(
    title="title", content="my first note",
)

# model is not in the database until it is saved
note.save()
print(note.id)

notes = Note.objects.all()

print(notes)

note = notes.first()

note.content = "my new content"

# update the note
note.save()

for note in notes:
    print(note.content)
    print(note.created_at)

