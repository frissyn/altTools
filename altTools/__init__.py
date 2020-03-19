try:
    import sys
    from time import sleep
    from collections import Counter
except ImportError as e:
    print('ImportError occured when initiating altTools:\n', str(e))

def write(values, pause=0.06, newline=True):
    for char in str(values):
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(pause)
    if newline == False: pass
    else: print()

def clr_input(prompt):
    blankSpace = ''
    placeholderVar = input("{0}".format(str(prompt)))
    for char in str(prompt):
        blankSpace += ' '
    for char in str(placeholderVar):
        blankSpace += ' '
    print("\033[A{0}\033[A".format(blankSpace), end='\n\r')
    return placeholderVar

def encrypt(value, shift):
    if type(shift) is not int:
        raise ValueError("'shift' paramter must be an integer value!")
    else: pass
    result = ""
    for i in range(len(value)):
        char = value[i]
        if: (char.isupper()): result += chr((ord(char) + shift - 65) % 26 + 65)
        else: result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def is_anagram(val1, val2):
    return Counter(str(val1)) == Counter(str(val2))

def del_duplicates(list1):
    if type(list1) is not list:
        raise ValueError("'list1' paramter must be a list value!")
    result = []
    for num in list1:
        if num not in result: result.append(num)
    if len(result) >= 1: return result
    else: return list1

def about():
    x = "altTools is Python Package created to contain a collection of\nunrealated and useful functions for a coder's convienience when needed.\nSome tools are pretty miscellaneous extras that do things like Ceasar\nCipher encryption and some tools have more useful applications like\nrandomly shuffling two iterable objects in the same order (not yet\nimplemented). A lot of these functions and tools already exist and are\nknown in the Python community elsewhere, but now you can find most of them\nin one place!"
    return x
