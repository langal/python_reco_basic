from pubsub import pub as queue

import ProductApplication
import RecommendationApplication

import DisplayUtils

# listeners that generates recommendations
def euclidian_listener(user):
    products = ProductApplication.get_products()
    strategy_name, best5, worst5 = RecommendationApplication.get_recommendations(user, ProductApplication.get_products(), 'euclidian')
    DisplayUtils.output(strategy_name, user, best5, worst5)

def cosine_listener(user):
    products = ProductApplication.get_products()
    strategy_name, best5, worst5 = RecommendationApplication.get_recommendations(user, ProductApplication.get_products(), 'cosine')
    DisplayUtils.output(strategy_name, user, best5, worst5)

def ham_listener(user):
    products = ProductApplication.get_products()
    strategy_name, best5, worst5 = RecommendationApplication.get_recommendations(user, ProductApplication.get_products(), 'hamming')
    DisplayUtils.output(strategy_name, user, best5, worst5)

queue.subscribe(euclidian_listener, 'user_took_quiz')
queue.subscribe(cosine_listener, 'user_took_quiz')
queue.subscribe(ham_listener, 'user_took_quiz')
