from math import log

def search (number: int, character: chr):

    rng = int(log(number, 2))
    for i in range(rng):

        if number % 128 == ord(character):
            return i

        number = number >> 1
        
    return -1
