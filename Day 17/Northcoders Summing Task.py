import random

nums_no_17 = []
for _ in range(1,101):
    nums_no_17.append(_)
nums_no_17.remove(17)
random.shuffle(nums_no_17)
print(nums_no_17)

nums_full = []
for _ in range(1,101):
    nums_full.append(_)
print(nums_full)

print(sum(nums_no_17))

big_number = len(nums_no_17)+1
print(big_number)
print(int(big_number*(big_number+1)/2))

nc_list = [4, 6, 3, 2, 5, 8]
print(sum(nc_list))

def find_missing_number(nums):
    ordered_nums = sorted(nums)
    print(ordered_nums)
    for index, number in enumerate(ordered_nums):
        if number == ordered_nums[index -1] + 2:
            return number - 1
    return None

print(find_missing_number(nc_list))

