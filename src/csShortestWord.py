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
    # #check for special chars
    
    # for string in input_str:
    #     if brk in string:
    #         brkPosition = input_str.find(brk)
    #         split_string1 = input_str.split(brk)
    #         shortest_word1 = len(min(split_string1, key = len))
    #         return shortest_word1
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

    



# print(csShortestWord('Always code as if the guy who ends up maintaining your code will be the most violent psychopath ever who knows where you live'))

print(csShortestWord('appleasdfasdfasdfabcde'))
# print(containsBrk('apple\tabcde'))