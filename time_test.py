import datetime

t = datetime.datetime.now()

k = t + datetime.timedelta.total_seconds(2600)

print(t)

print(t.time())
print(k.time())