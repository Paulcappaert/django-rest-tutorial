from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['title', 'content']
        read_only_fields = ['user', 'created_at']
