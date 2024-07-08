from django.urls import path

from snippets.views.snippet_detail_api_view import SnippetDetailApiView
from snippets.views.snippet_list_api_view import SnippetListApiView
from snippets.views.user_list_serializer import UserListApiView

urlpatterns = [
    path('snippets', SnippetListApiView.as_view()),
    path('snippets/<int:pk>', SnippetDetailApiView.as_view()),
    path('users', UserListApiView.as_view()),
]
