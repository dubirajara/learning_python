'''
write a function that takes a String and returns an
list with the length of each word added to each element.
'''


def add_length(words):
    words_len = [[i, str(len(i))] for i in words.split()]
    return [' '.join(i) for i in words_len]   


assert add_length('carrot cake') == ['carrot 6', 'cake 4']  # testcase
