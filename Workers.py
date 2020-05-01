from pubsub import pub as queue

import RecommendationCalculator

import DisplayUtils

# listeners that generates recommendations
def euclidian_listener(user):
    strategy_name, best5, worst5 = RecommendationCalculator.get_recommendations(user, 'euclidian')
    DisplayUtils.output(strategy_name, user, best5, worst5)

def cosine_listener(user):
    strategy_name, best5, worst5 = RecommendationCalculator.get_recommendations(user, 'cosine')
    DisplayUtils.output(strategy_name, user, best5, worst5)

def ham_listener(user):
    strategy_name, best5, worst5 = RecommendationCalculator.get_recommendations(user, 'hamming')
    DisplayUtils.output(strategy_name, user, best5, worst5)

queue.subscribe(euclidian_listener, 'user_took_quiz')
queue.subscribe(cosine_listener, 'user_took_quiz')
queue.subscribe(ham_listener, 'user_took_quiz')
