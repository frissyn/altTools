import sys
from time import sleep

class altTools:
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
        print("\033[A{0}\033[A".format(blankSpace), end='\r')
        return placeholderVar

    def encrypt(value, shift):
        if type(shift) is not int:
            raise ValueError("\'shift\' paramter must be an integer value!")
        else: pass
        result = ""
        for i in range(len(value)):
            char = value[i]
            if (char.isupper()):
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else: 
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result
