from django.urls import path

from snippets.views.snippet_list_api_view import SnippetListApiView

urlpatterns = [
    path('', SnippetListApiView.as_view())
]
