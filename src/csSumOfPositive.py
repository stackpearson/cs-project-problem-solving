# Given an array of integers, return the sum of all the positive integers in the array.

# Examples:

# csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
# csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
# csSumOfPositive([-3, -2]) -> 0

def csSumOfPositive(input_arr):
    positive_nums = []
    for num in input_arr:
        if num > 0:
            positive_nums.append(num)

    return sum(positive_nums)

print(csSumOfPositive([2, 3, -3, 5, 10]))
