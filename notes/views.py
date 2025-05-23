from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework import filters

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # search by keyword

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        # Ensure users can only access their own notes
        return Note.objects.filter(user=self.request.user)