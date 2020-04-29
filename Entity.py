import json

"""
Product and Users can inherit a "Tag" mixin or implement a simple Tag interface.
"""
class AttributedEntity(object):

    def __init__(self, tags):
        self.tags = tags  # tags are implemented as simple key->value pairs ('formal': 95; 'punk': 15)

    def __str__(self):
        return json.dumps(self.tags)
