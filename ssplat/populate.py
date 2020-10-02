import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ssplat.settings')

import django
import datetime
import dateutil.parser
django.setup()
import json
from news.models import ArticleSource, Articles, Author

f = open('articles.json',)
json_object = json.loads(f.read())

for obj in json_object:
    dt = dateutil.parser.parse(obj['publishedAt'])
    author = Author.objects.get_or_create(author_name=obj["author"])[0]
    if(obj['source']['id']==None):
        art_src = ArticleSource.objects.get_or_create(source_id="unknown", source_name=obj["source"]["name"])[0]
        Articles.objects.get_or_create(source=art_src,
                                       author=author,
                                       title=obj["title"],
                                       Desc=obj["description"],
                                       url=obj["url"],
                                       url_image=obj['urlToImage'],
                                       date=dt,
                                       content=obj["content"])
    else:
        art_src = ArticleSource.objects.get_or_create(source_id=obj["source"]["id"], source_name=obj["source"]["name"])[0]
        Articles.objects.get_or_create(source=art_src,
                                       author=author,
                                       title=obj["title"],
                                       Desc=obj["description"],
                                       url=obj["url"],
                                       url_image=obj['urlToImage'],
                                       date=dt,
                                       content=obj["content"])
    