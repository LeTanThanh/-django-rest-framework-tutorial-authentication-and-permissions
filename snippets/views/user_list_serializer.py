from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from snippets.serializers.user_serializer import UserSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
