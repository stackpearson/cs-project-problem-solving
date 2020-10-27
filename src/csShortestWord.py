# Given a string of words, return the length of the shortest word(s).

# Notes:

# The input string will never be empty and you do not need to validate for different data types.

def containsBrk(st):
    brk = '\t'
    for char in st:
        if brk in st:
            return True
        else:
            return False

def csShortestWord(input_str):

    brk ='\t'
    if containsBrk(input_str):
        brkPosition = input_str.find(brk)
        split_string1 = input_str.split(brk)
        shortest_word1 = len(min(split_string1, key = len))
        return shortest_word1
   
    else:
        split_string2 = input_str.split(" ")
        shortest_word2 = len(min(split_string2, key = len))
        return shortest_word2


print(csShortestWord('appleasdfasdfasdf\tabcde'))