# 2'50

# FIFO - tj First In Firs Out

# ako bi htjeli micati prvi objekt velikih lista, puno treba uciniti da se svi itemi pomaknu i promjene idexe itd. Zato imamo "deque" modul

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)    # deque([2, 3])
if not queue:
    print("empty")

