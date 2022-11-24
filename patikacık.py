"""

n = int(input())
n = n +1

for i in range(1,n,1):
    print (i, end="")

"""


def is_leap(year):
    leap = False

    if 0 == year%4 and year%4 != year%100 or year%4 == year%400 :

            leap =True

    return leap


year = int (input ())
print (is_leap (year))
