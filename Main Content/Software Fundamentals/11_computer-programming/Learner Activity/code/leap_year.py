# Leap-year checker (Study Guide p. 71).
# Rule: divisible by 4, except years divisible by 100, unless also divisible by 400.

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


for y in [2000, 1900, 2024, 2023]:
    print(y, is_leap(y))
