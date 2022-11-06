
#one of possible ways to create a list with week days
# import calendar
# day_names = list(calendar.day_name)

day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dictionary_1 = {i+1: day_names[i] for i in range(7)}
dictionary_2 = {day_names[i]: i+1 for i in range(7)}

print(dictionary_1)
print(dictionary_2)

