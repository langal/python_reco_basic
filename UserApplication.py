"""
This basically models a User module or application.
"""

import os
from Tags import get_random_tags
from Entity import AttributedEntity

"""
A very simplified representation of a User
"""
class User(AttributedEntity):
    pass


def get_user():
    tags = get_random_tags()
    user = User(tags)
    return user
