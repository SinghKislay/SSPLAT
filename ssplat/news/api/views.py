from rest_framework import generics, views
from rest_framework.response import Response
from news.models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse

class SourceView(generics.ListAPIView):
    serializer_class = ArticlesSerializer
    def get_queryset(self):
        sname = self.request.query_params.get('sname')
        sname = ArticleSource.objects.filter(source_id=sname)[0]
        return Articles.objects.filter(source=sname)

class AuthorQueryView(generics.ListAPIView):
    serializer_class = ArticlesSerializer
    def get_queryset(self):
        aname = self.request.query_params.get('aname')
        aname = Author.objects.filter(author_name=aname)[0]
        return Articles.objects.filter(author=aname)

class AuthorView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class ArticleCountView(views.APIView):
    def get(self, request, *args, **kwargs):
        count = Articles.objects.all().count()
        data = {"totalarticleCount": count}
        return JsonResponse(data, safe=False)

class ArticleCountBySourceView(views.APIView):
    def get(self, request, *args, **kwargs):
        aname = self.request.query_params.get('aname')
        auth = Author.objects.filter(author_name=aname)[0]
        count = Articles.objects.filter(author=auth).count()
        data = {"articleCountbyAuthor": count}
        return JsonResponse(data, safe=False)