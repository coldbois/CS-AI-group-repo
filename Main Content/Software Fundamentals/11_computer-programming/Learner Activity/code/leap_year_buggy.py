# The buggy checker from the Bug Hunt activity (2.3).
# It runs without any error message, but one of these answers is wrong. Which one?

def is_leap(y):
    return y % 4 == 0


for y in [2000, 1900, 2024, 2023]:
    print(y, is_leap(y))
