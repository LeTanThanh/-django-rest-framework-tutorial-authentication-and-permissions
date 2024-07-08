from rest_framework.serializers import ModelSerializer

from snippets.models.snippet import Snippet


class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'ttile', 'code', 'linenos', 'language', 'style']
