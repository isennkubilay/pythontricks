#Write a Python program to calculate number of days between two dates.

from datetime import date
f_date = date(2019, 5, 29)
l_date = date(2019, 6, 1)
delta = l_date - f_date
print(delta.days)
