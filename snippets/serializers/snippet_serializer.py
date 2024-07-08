from rest_framework.serializers import ModelSerializer

from snippets.models.snippet import Snippet


class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
