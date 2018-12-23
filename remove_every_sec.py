'''
Take a list and remove every second element out of that list.
Always keep the first element and start removing with the next element.
'''


def remove_every_sec(my_list):
    sec_elements = [j for i, j in enumerate(my_list) if i % 2 == 0]
    return sec_elements


assert remove_every_sec(['a', 'b', 'c', 'd', 'e']) == ['a', 'c', 'e']
