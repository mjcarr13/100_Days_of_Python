import math
checklist = []


def is_prime(num):
    if num == 2:
        return True
    elif num == 1 or num > 2 and num % 2 == 0:
        return False
    else:
        checklist = list(range(2, math.floor(num / 2)))
        print(checklist)
        for i in checklist:
            if num % i == 0:
                return False
            else:
                return True

print(is_prime(73))
print


