# 2'41

from datetime import datetime, timedelta

# timedelta za trajanje - duration

dt1 = datetime(2020, 7, 29)
dt2 = datetime.now()
# da bi bilo jasnije sto broj predtavlja bolje ga je stavljati kao keyword-argument, npr
dt3 = dt1 + timedelta(1)
dt4 = dt1 + timedelta(days=1, minutes=5)
print(dt3)  # 2020-07-30 00:00:00

duration = dt2 - dt1
print(duration)  # 730 days, 18:46:24.795260
print("days", duration.days)  # days 730
print("seconds", duration.seconds)  # seconds 67802
# total_seconds 63139802.029525
print("total_seconds", duration.total_seconds())
