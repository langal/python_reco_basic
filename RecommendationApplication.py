"""
This models a Recommendation module or application.
"""
import heapq
import json

from Strategies import *

"""
This class basically needed to leverage the "heap" library.

It basically represents the distance between two objects (eg. User or Products).
"""
class Distance(object):

    def __init__(self, obj1, obj2, distance):
        self.obj1 = obj1
        self.obj2 = obj2
        self.distance = distance

    # used in heap operation
    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        attributes = {
            'distance': self.distance,
            'product': self.obj2.tags
        }
        return json.dumps(attributes)

"""
A generic "get_distance" handler could dynamially load different distance strategies.
"""
def get_single_distance(object1, object2, strategy):
    DISTANCE_FUNCTION = globals()[strategy]
    return DISTANCE_FUNCTION(object1, object2)

"""
This gets the distances between one objects (ie. a User) and many objects (ie. Products)
"""
def get_recommendations(user, products, strategy):
    distances = []
    for product in products:
        distance = Distance(user, product, get_single_distance(user, product, strategy))
        heapq.heappush(distances, distance)

    best5 = heapq.nsmallest(5, distances)
    worst5 = heapq.nlargest(5, distances)

    return (strategy.upper(), best5, worst5)
