def str2bin(text):
    str_bin = '\n'.join('{:08b}'.format(ord(s)) for s in text)
    print(str_bin)


if __name__ == '__main__':
    str2bin(input(''))
