

from elasticsearch_dsl import DocType, Index, Text, Object, Keyword, Search, GeoShape, Nested
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from django.db import models

connections.create_connection()

class ReviewDoc(DocType):
    summary = Text()
    username = Object(properties={'username':Keyword()})    
    location = Nested(properties={'polygon':GeoShape()})    
    class Meta:
        index = 'review-index'

'''
search for the words in the summary field of the review
'''

def search_review(review):
    s = Search().filter('term', summary=review)
    response = s.execute()
    return response

'''
Filter the user
'''
def search_user(user):
    s = Search().filter('term', user__username=user)
    response = s.execute()
    return response

'''
Range date search on the "published" field
'''

def search_date_range(gte_date, lte_date):
    s = Search().filter('range', published={'gte':gte_date, 'lte':lte_date})
    response = s.execute()
    return response
