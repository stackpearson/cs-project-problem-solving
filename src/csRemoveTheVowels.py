# Given a string, return a new string with all the vowels removed.

# Examples:

# csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
# Notes:

# For this challenge, "y" is not considered a vowel.

def csRemoveTheVowels(input_str):
    #keep a list of the letters in our new string
    new_string = ""

    # declare our vowels
    vowels ="AEIOUaeiou"
    
    #iterate over our string to find vowels
    for char in input_str:
        if char not in vowels:
            new_string = new_string + char

    return new_string

    #remove vowels
    #return a string with the vowels removed

print(csRemoveTheVowels("a b y e"))