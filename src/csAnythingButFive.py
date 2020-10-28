# Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

# Examples:

# csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
# csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
# csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
# Notes:

# The output can contain the digit 5.
# The start number will always be less than the end number (both numbers can also be negative).

def csAnythingButFive(start, end):
    allNums = [str(num) for num in range(start, end + 1)]
    filteredNums = []
    omit = '5'
    for num in allNums:
        if (omit not in num):
            filteredNums.append(num)

    return len(filteredNums)

print(csAnythingButFive(-5, 15))