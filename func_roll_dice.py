"""Produce a dice roll."""

import random

__author__ = "6611082: Cedric Reuter, 6317302: Fabian Eichner"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = " " 
__email__ = " " 

# EPR_03

def roll_dice(number=1, faces=6, seed=None):
    """Produce string with results of dice rolls (with a number of dice rolls \
    specified in the input variable number and possible results determined by \
    the range between 1 and input variable faces. Allowed range of number is \
    [1, 10] and faces [2, 100]"""
    
    if type(number) == int and type(faces) == int:
        if 1 <= number <= 10 and 2 <= faces <= 100:
            result = []
            random.seed(seed, version=2)
            for count in range(0, number):
                result.append(str(random.randint(1, faces)))
            result_string = ', '.join(result)
            return (result_string)
        else:
            print('ERROR')
    else:
        print('ERROR')


