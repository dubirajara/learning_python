"""
We have a string s
We have a number n

Create a function string_n_string(s, n) that takes your string, 
concatenates the even-indexed chars to the front, odd-indexed chars to the back
and return the result of the string after applying the function to it n times.
"""


def string_n_string(s, n):
    for _ in range(n):
        even = [char for i, char in enumerate(s) if i % 2 == 0]
        odd = [char for i, char in enumerate(s) if i % 2 != 0]
        s = ''.join(even + odd)

    return s


assert string_n_string("Wow Example!", 1) == "WwEapeo xml!"  # testcase
assert string_n_string("qwertyuio", 2) == "qtorieuwy"  # testcase
