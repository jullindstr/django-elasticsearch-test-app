from datetime import datetime 
import random
from app.models import Review, User, Location
from django.contrib.gis.geos import Point, Polygon
import names
from factory.fuzzy import BaseFuzzyAttribute
import factory.django, random


def random_poly(n):
    points = []
    for i in range(0,n):
        p = Point(random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0))
        points.append(p)
    points[0] = points[-1] 
    p = Polygon(points)
    l = Location(polygon=p)
    return l


def random_date():
    y = random.randint(2000,2018)
    m = random.randint(1,12)
    d = random.randint(1,28)
    return datetime(y,m,d)


def create_user():
    u = User(username=names.get_first_name().lower())
    return u



def create_review():
    reviews = ('positive review', 'negative review', 'angry review', 'neutral review', 'emotional review', 'funny review','facinating','interesing','unusual','boring','nice')
    n = random.randint(0,len(reviews)-1)
    u = create_user()
    p = random_poly(random.randint(4,6))
    p.save()
    u.save()
    r = Review(summary=reviews[n], user=u, published=random_date(), location=p)
    return r

   
