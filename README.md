# python_reco_basic

This is a very simple simulation of a Recommendation system - matching a User to Products.

**ProductApplication.py**(ProductApplication.py) models a product service and returns a list of *Products*.

**UserApplication.py** models a user service and provides a function to get a *User*.

Both **Users** and **Products** inherit the *Entity.AttributedEntity*.   They merely contain a set of "tags".

**Tags.py** contains a list of tag-types (eg. "formal", "retro", "blue", etc.) and 
provides a function to return a random set of tags with random values.

**Strategies.py** contains functions to calculate the Euclidian distance, Cosine similarity, and Hamming distance between
two objects that have tags.

**RecommendationApplication.py** provides functions to get "recommendations" based on the function in **Strategies.py**.

**Workers.py** provides handler functions to handle events.

simluate.py is basically a test program which dumps users in q simple memory based PubSub (https://pypi.org/project/PyPubSub/).

Listeners are implemnted using the 3 stratgies from **Strategies.py** and 
results are just dumped to standard out using some DislayUtil function.
