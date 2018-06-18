# -*i- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models as geomodels
import json
from datetime import datetime
from django.db import models
from elasticsearch_dsl.connections import connections

#from django_elasticsearch_dsl.signals import BaseSignalProcessor 
#from django.dispatch import Signal
from search.search import ReviewDoc


class Location(geomodels.Model):
    polygon = geomodels.GeometryField()
    def to_index(self):
        if(not self.polygon is None): 
            return json.loads(self.polygon.json)
        else:
            return []


class User(models.Model):
    username = models.CharField(max_length=15)
    def to_index(self):
        return {
            'username':self.username,
            }

    def __str__(self):
        return str(self.username)


class Review(models.Model):
    summary = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True, default=datetime.now())
    location = models.ForeignKey(Location, blank=True, null=True)
    def to_index(self):
        data = {
                #'_id' = self.pk
                #'id' = self.pk
                'summary':self.summary,
                'user':self.user.to_index(),
                'published':self.published.isoformat(),
                'location':self.location.to_index()
                }
        if (not self.location is None):
            data['location'] = self.location.to_index()
        else: data['location'] = []
        return ReviewDoc(meta={'id':self.id,}, **data)
  
    def save(self, elasticsearch, *args, **kwargs):
        if elasticsearch == False:
            return super(Review, self).save(*args, **kwargs)
        else:
                     
            super(Review, self).save(*args, **kwargs)
            return update_search(self)
   
    #        Signal.disconnect(BaseSignalProcessor().handle_save(), sender=Review)
    
    def __str__(self):
        return '%s/%s/%s' %(self.summary, self.user, self.published)


def update_search(instance, **kwargs):
    #delete index before saving, ignore if it does not exist index.delete(ignore404)
    
    instance.to_index().save(using=connections.get_connection(),index='review-index')


def save(instance, elasticsearch, *args,**kwargs):
    if elasticsearch == False:
        return super(instance, self).save(*args,**kwargs)
    else: 
        #return post_save.connect(update_search, sender = Review)
        return update_search()


