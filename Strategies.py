import numpy as np
import scipy.spatial.distance

"""
These function model different recommendation strategies
"""

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
