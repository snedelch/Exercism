"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param: elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO: define the 'preparation_time_in_minutes()' function
#   and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers: int):
    """Calculating the preparation time.

    :param: layers: int - number of layers we add to the lasagna.
    :return: int - 'PREPARATION_TIME' times the layers.

    Function that takes the number of layers you want to add to the lasagna as an
    argument and returns how many minutes you would spend making them.
    """
    return PREPARATION_TIME * layers


# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Return elapsed cooking time.

    :param: number_of_layers: int - number of layers we add to the lasagna.
    :param: elapsed_bake_time: int - the time we already have been cooking.
    :return: int - the total time it took to cook so far.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
