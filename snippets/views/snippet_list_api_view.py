from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models.snippet import Snippet
from snippets.serializers.snippet_serializer import SnippetSerializer


class SnippetListApiView(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return Response(data=serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
