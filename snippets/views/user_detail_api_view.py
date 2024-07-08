from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView

from snippets.serializers.user_serializer import UserSerializer


class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
