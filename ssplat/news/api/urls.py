from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path

urlpatterns = [
    path("sources", SourceView.as_view()),
    path("authors", AuthorView.as_view()),
    path("q_author", AuthorQueryView.as_view()),
    path("article_count", ArticleCountView.as_view()),
    path("art_author", ArticleCountBySourceView.as_view())
]