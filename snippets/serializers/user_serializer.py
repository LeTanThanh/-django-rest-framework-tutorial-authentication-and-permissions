from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from snippets.models.snippet import Snippet


class UserSerializer(ModelSerializer):
    snippets = PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
