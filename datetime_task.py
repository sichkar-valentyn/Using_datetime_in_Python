# File: Using_datetime_in_Python.py
# Description: Using datetime in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# ### Reference to:
# [1] Valentyn N Sichkar. Using datetime in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Using_datetime_in_Python (date of access: XX.XX.XXXX)



# Implementing the task with module datetime
import datetime

# Input the string with date in format - year month day
date = [int(i) for i in input().split()]

# Converting and saving the format date in the class datetime.date
current_date = datetime.date(date[0], date[1], date[2])

# Input the amount of days to add to the saved date
add = int(input())

# Converting the adding days into the date format
add_days = datetime.timedelta(add)

# Calculating the final result
future_date = current_date + add_days

# Showing the final date
print(future_date.year, future_date.month, future_date.day)
