from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models.snippet import Snippet
from snippets.serializers.snippet_serializer import SnippetSerializer


class SnippetDetailApiView(APIView):
    def get(self, request, pk, format=None):
        self._get_snippet(pk=pk)
        serializer = SnippetSerializer(instance=self._snippet)
        return Response(data=serializer.data)

    def put(self, request, pk, format=None):
        self._get_snippet(pk=pk)
        serializer = SnippetSerializer(self._snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self._get_snippet(pk=pk)
        self._snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_snippet(self, pk):
        try:
            self._snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
