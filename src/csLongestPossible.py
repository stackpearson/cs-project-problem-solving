# Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

# Examples:

# csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
# csLongestPossible("abc", "abc") -> "abc"

def csLongestPossible(str_1, str_2):
    combined = set((str_1 + str_2))
    reduced = ''
    final = ''
    for i in combined:
        if(i in reduced):
            pass
        else:
            reduced=reduced+i
    sorted_results = sorted(reduced)
    
    return final.join(sorted_results)

print(csLongestPossible('abcd', 'abcdefgh'))