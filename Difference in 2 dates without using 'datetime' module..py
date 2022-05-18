#Find difference between 2 dates without using datetime module.

#user input
d1, m1, y1 = [int(i)for i in input().split('/')]

d2, m2, y2 = [int(i) for i in input().split('/')]

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

leap_months = months

leap_months[1] += 1

s1 = 0

s2 = 0

#function to check leap year

def is_leap(year):
    return (year % 4 ==0 and year % 100 > 0) or (year % 400 != 0)

for a in range(y1):
    s1 += 366 if is_leap(a) else 365

for b in range(y2):
    s2 += 366 if is_leap(a) else 365


s1 += leap_months[m1] if is_leap(y1) else months[m1]

s2 += leap_months[m2] if is_leap(y2) else months[m2]

s1 += d1

s2 += d2

#Now we have the total days in both dates.

print(abs(s1 - s2)) #The difference in days
