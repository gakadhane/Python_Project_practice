weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
weekdays_dict = {}

for day in weekdays:
    if day in weekdays_dict:
        weekdays_dict[day] += 1
    else:
        weekdays_dict[day] = 1

print(weekdays_dict)
