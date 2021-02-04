from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()

    def create(self, validated_data):
        return Note.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
        )

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()
        return instance