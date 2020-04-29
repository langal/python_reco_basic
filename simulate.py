import os
import time

from pubsub import pub

import ProductApplication
import UserApplication
import RecommendationApplication
import DisplayUtils

# listeners that generates recommendations
def euclidian_listener(user):
    products = ProductApplication.get_products()
    strategy_name, best5, worst5 = RecommendationApplication.get_recommendations(user, ProductApplication.get_products(), 'euclidian')
    output(strategy_name, user, best5, worst5)

def cosine_listener(user):
    products = ProductApplication.get_products()
    strategy_name, best5, worst5 = RecommendationApplication.get_recommendations(user, ProductApplication.get_products(), 'cosine')
    output(strategy_name, user, best5, worst5)

def ham_listener(user):
    products = ProductApplication.get_products()
    strategy_name, best5, worst5 = RecommendationApplication.get_recommendations(user, ProductApplication.get_products(), 'hamming')
    output(strategy_name, user, best5, worst5)

def output(strategy_name, user, best5, worst5):
    DisplayUtils.bold("USER {}".format(user))
    DisplayUtils.green(strategy_name + " CLOSEST 5 products")
    [DisplayUtils.green(str(good)) for good in best5]
    DisplayUtils.yellow(strategy_name + " FARTHEST 5 products")
    [DisplayUtils.yellow(str(bad)) for bad in worst5[::-1]]

pub.subscribe(euclidian_listener, 'user_took_quiz')
pub.subscribe(cosine_listener, 'user_took_quiz')
pub.subscribe(ham_listener, 'user_took_quiz')

NUM_USERS = int(os.environ.get('NUM_USERS', 10))
for x in range(0, NUM_USERS):
    print("\n\n\n")
    time.sleep(3)
    user = UserApplication.get_user()
    pub.sendMessage('user_took_quiz', user=user)
