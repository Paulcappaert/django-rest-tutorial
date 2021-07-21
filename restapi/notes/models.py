from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from notes.inner_models import Edits


class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    _edits = models.JSONField()

    _inner_edits = None

    @property
    def edits(self):
        if self._inner_edits is None:
            self._inner_edits = Edits.parse_raw(self._edits)

        return self._inner_edits

    def save(self, *args, **kwargs):
        if self._inner_edits:
            self._edits = self._inner_edits.json()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
