__author__ = "6611082: Cedric Reuter, 6317302: Fabian Eichner"


# EPR_03

def roll_cheating_dice(number=1, seed=None):
    """Produce string with results of dice rolls (with a number of dice rolls \
    specified in the input variable number and possible results determined by \
    the range between 1 and input variable faces. Allowed range of number is \
    [1, 10]. The probability of obtaining a 3 with the dice roll is doubled \
    compared to the other possible outcomes"""
    import random

    if type(number) == int:
        if 1 <= number <= 10:
            faces = (1, 2, 3, 4, 5, 6)
            result = []
            random.seed(seed, version=2)
            for count in range(0, number):
                ran_result = random.choices(faces, [5, 5, 10, 5, 5, 5])
                result.append(str(ran_result[0]))
            result_string = ', '.join(result)
            return (result_string)
        else:
            print('ERROR')
    else:
        print('ERROR')


out = roll_cheating_dice(3, None)
print(out)
