
from app import models
from search import ReviewDoc
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from datetime import datetime
import random

def bulk_reindex():
    ReviewDoc.init()
    client = connections.get_connection()
    for r in models.Review.objects.all().iterator():
        r.to_index().save(using=connections.get_connection(),index='review-index')
        bulk(client=client, actions=[r.to_index().to_dict(include_meta=True)] )




  


