import sys
from time import sleep

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
        if (char.isupper()): result += chr((ord(char) + shift - 65) % 26 + 65)
        else: result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def about():
    x = "altTools is Python Package created to contain a collection of\nunrealated and useful functions for a coder's convienience when needed.\nSome tools are pretty miscellaneous extras that do things like Ceasar\nCipher encryption and some tools have more useful applications like\nrandomly shuffling two iterable objects in the same order (not yet\nimplemented). A lot of these functions and tools already exist and are\nknown in the Python community elsewhere, but now you can find most of them\nin one place!"
    return x

def info():
    functions = ['write(value, pause=0.06, newline=True)', 'clr_input(prompt)', 'encrypt(value, shift)']
    descriptions = [
        'Prints out values to the stream and pauses shortly between each value to create a typewriter effect.',
        'Works like a regular input statement, but clears the prompt and input value after a newline key is pressed.',
        'Returns a Ceasar Cipher encrypted version of a string corresponding to the shift prameter value.'
    ]
    table = 'Description of altTools functions:\n\n'

    if len(functions) == len(descriptions):
        for i in range(len(functions)):
            table += str(functions[i]) + ' : ' + str(descriptions[i]) + '\n'
            return table
    else: return "find more information at 'https://pypi.org/project/altTools/'"
