# 5'05

from datetime import datetime
import time


dt1 = datetime(2022, 7, 29)
print(dt1)

dt2 = datetime.now()
print(dt2)

dt3 = datetime.strptime("2022/07/29", "%Y/%m/%d")
print(dt3)

dt4 = datetime.fromtimestamp(time.time())
print(dt4)

# goglanje za "python 3 strptime" dolazimo do https://docs.python.org/3/library/datetime.html na cijem dnu ima tablica uputa sa %kodovima.

print(dt1, dt2, dt3, dt4)
# 2022-07-29 00:00:00 2022-07-29 18:36:54.370866 2022-07-29 00:00:00 2022-07-29 18:36:54.376081

print(f"{dt1.year}/{dt1.month}")    # 2022/7

print(dt1 > dt2)  # False
