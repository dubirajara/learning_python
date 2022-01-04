'''
write a function that takes a String and returns an
list with the length of each word added to each element.
'''


def add_length(words):
    return [f'{i} {str(len(i))}' for i in words.split()]  


assert add_length('carrot cake') == ['carrot 6', 'cake 4']  # testcase
