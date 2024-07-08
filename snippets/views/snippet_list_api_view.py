from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models.snippet import Snippet
from snippets.serializers.snippet_serializer import SnippetSerializer


class SnippetListApiView(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return Response(data=serializer.data)
