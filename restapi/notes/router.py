from .api import NoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='note')
urlpatterns = router.urls