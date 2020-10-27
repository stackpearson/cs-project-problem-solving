# Given a string of words, return the length of the shortest word(s).

# Notes:

# The input string will never be empty and you do not need to validate for different data types.

def csShortestWord(input_str):
    # convert our string to a list of strings
    split_string = input_str.split(" ")
    # determine the length of shortest word
    shortest_word = len(min(split_string, key = len))
    # return the length of the shortest element
    return shortest_word



print(csShortestWord('Always code as if the guy who ends up maintaining your code will be the most violent psychopath ever who knows where you live'))