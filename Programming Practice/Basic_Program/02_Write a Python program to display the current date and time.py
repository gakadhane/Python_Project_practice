import datetime

now = datetime.datetime.now()
print("Current date and time:")

print(now.strftime("%Y-%M-%D %H:%M:%S"))

print(now.time())

print(now.date())

print(now.__hash__())

print(now.ctime())
