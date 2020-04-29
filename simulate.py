import os
import time

from pubsub import pub as queue

import UserApplication

# this is just a hack to run the static code in Workers to get them to subscribe to the queue
import Workers

NUM_USERS = int(os.environ.get('NUM_USERS', 10))
for x in range(0, NUM_USERS):
    print("\n\n")
    time.sleep(2)
    user = UserApplication.get_user()
    queue.sendMessage('user_took_quiz', user=user)
