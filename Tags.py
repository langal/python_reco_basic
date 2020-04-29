"""
This module basically generates random attributes and tags.
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

"""
This function just generates a set of random tags and scores.

In real-life, this would be a Query from some data source.
"""
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

    flexible_tags = {
        style: random.randint(80, 100),
        primary_color: random.randint(80, 100),
        secondary_color: random.randint(30, 60)
    }

    flexible_tags.update(other_flexible_tags)
    return flexible_tags
