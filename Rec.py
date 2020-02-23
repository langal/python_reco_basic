import heapq
import scipy.spatial.distance
import numpy as np
import json
import sys
from sklearn.metrics.pairwise import cosine_similarity

TAGS = False

BOLD = '\033[1m' + '\033[4m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'

"""
Product and Users can inherit a "Tag" mixin or implement a simple Tag interface.
"""
class AttributedEntity(object):

    def __init__(self, tags):
        self.tags = tags

    def __str__(self):
        return json.dumps(self.tags)


"""
This class in not necessary.  I basically needed something that implements "__lt__" to take advantage of HEAPS.
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
A generic "get_distance" handler could dynamially load different algorithms
"""
def get_distance(object1, object2, algo):
    DISTANCE_FUNCTION = globals()[algo]
    return DISTANCE_FUNCTION(object1, object2)


"""
Euclidian Distance implementation.
"""
def euclidian(object1, object2):
    all_keys = set(object1.tags.keys()).union(set(object2.tags.keys()))
    vector1 = []
    vector2 = []
    for key in all_keys:
        """
        Basically, make an n-dimensional vector.  A dimention is a key like 'formal'.  The 'rating' is the distance is goes to that dimenion.
        """
        vector1.append(object1.tags.get(key, 0.0))
        vector2.append(object2.tags.get(key, 0.0))

    """
    This magic function calculates the distance between 2 vectors.
    """
    return scipy.spatial.distance.euclidean(vector1, vector2)

"""
Cosine similarity implementation.
"""
def cosine(object1, object2):
    all_keys = set(object1.tags.keys()).union(set(object2.tags.keys()))
    vector1 = []
    vector2 = []
    for key in all_keys:
        """
        Basically, make an n-dimensional vector.  A dimention is a key like 'formal'.  The 'rating' is the distance is goes to that dimenion.
        """
        vector1.append(object1.tags.get(key, 0.0))
        vector2.append(object2.tags.get(key, 0.0))
    return scipy.spatial.distance.cosine(vector1, vector2)


"""
Hamming distance implementation.
"""
def hamming(object1, object2):
    all_keys = set(object1.tags.keys()).union(set(object2.tags.keys()))
    vector1 = []
    vector2 = []
    for key in all_keys:
        """
        Basically, make an n-dimensional vector.  A dimention is a key like 'formal'.  The 'rating' is the distance is goes to that dimenion.
        """
        vector1.append(key in object1.tags.keys())
        vector2.append(key in object2.tags.keys())
    return scipy.spatial.distance.hamming(vector1, vector2) 


"""
List of attribute types
"""
import random

styles = [
    'formal',
    'punk',
    'country',
    'retro',
    'elegant',
    'sexy',
    'victorian',
]

colors = [
    'black',
    'white',
    'blue',
    'red',
    'yellow',
    'silver',
    'gold'
]

other = [
    'spring',
    'summer',
    'winter',
    'autumn',
]

all_tags = other + colors + styles

def get_random_tags():
    """
    Pick a random style and 2 random colors
    """
    style = styles[random.randrange(len(styles))]
    primary_color = colors[random.randrange(len(colors))]
    secondary_color = None
    secondary_color = colors[random.randrange(len(colors))]
    while secondary_color == primary_color:
        secondary_color = colors[random.randrange(len(colors))]

    """
    Pick some other random attributes
    """
    other_tags_count = random.randrange(5)
    other_tags = {}
    other_flexible_tags = {}
    for i in range(other_tags_count):
        random_tag = all_tags[random.randrange(len(all_tags))]
        if random_tag in (style, primary_color, secondary_color):
            continue
        other_tags[random_tag] = 1
        other_flexible_tags[random_tag] = random.randint(10, 100)

    tags = {
        style: 1,
        primary_color: 1,
        secondary_color: 1,
    }
    flexible_tags = {
        style: random.randint(80, 100),
        primary_color: random.randint(80, 100),
        secondary_color: random.randint(30, 60)
    }
    tags.update(other_tags)

    if TAGS:
        return tags

    flexible_tags.update(other_flexible_tags)
    return flexible_tags

"""
Colored Output
"""
def bold(string):
    print(BOLD + str(string) + END)

def green(string):
    print(GREEN + str(string) + END)

def yellow(string):
    print(YELLOW + str(string) + END)

"""
Make X number of "products" with random tags
"""
NUM_PRODUCTS = int(sys.argv[1])
products = []
for i in range(0, NUM_PRODUCTS):
    tags = get_random_tags()
    products.append(AttributedEntity(tags))

"""
Make X number of Users with random tags and get distance to each product.
"""
NUM_USERS = 1
for i in range(0,NUM_USERS):
    tags = get_random_tags()
    user = AttributedEntity(tags)

    print("\n\n")

    for algo in ("euclidian", "cosine", "hamming"):
        distances = []
        for product in products:
            distance = Distance(user, product, get_distance(user, product, algo))
            heapq.heappush(distances, distance)
    
        bold("USER {}".format(user))
        green(algo.upper() + " CLOSEST 5 products")
        best5 = heapq.nsmallest(5, distances)
        [green(str(good)) for good in best5]
        yellow(algo.upper() + " FARTHEST 5 products")
        worst5 = heapq.nlargest(5, distances)
        [yellow(str(bad)) for bad in worst5[::-1]]
        print()
