'''
count the total number of lowercase letters in a string
'''


def count_lowercase_letters(string):
    lower_letters = [s for s in string if s.islower()]
    return len(lower_letters)


assert count_lowercase_letters("abcDEFG123") == 3 # testcase
