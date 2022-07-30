# 2'09

import time

print(time.time())  # 1659111044.3255548 (sek od 1.1.1970)


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)  # 0.0002090930938720703
