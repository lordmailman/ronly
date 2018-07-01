#! python3
"""Define Dice classes."""

from random import randint
from math import isclose

class Die(object):
    """Basic Die object with list of values."""

    def __init__(self, num_sides=None):
        """Create with sides from 1 to <num_sides>."""
        # Handle input
        if not isinstance(num_sides, int):
            raise TypeError('num_sides of Die must be an integer.')
        elif num_sides < 0:
            raise ValueError('num_sides of Die must be >= 0.')

        self.values = range(1, 1+num_sides)
        """Range of face values"""

        if num_sides == 0:
            values = [0]
        else:
            values = self.values

        # Calculate properties
        len_values = len(values)
        self._max_value = max(values)
        self._min_value = min(values)
        self._mean_value = (self._max_value + self._min_value)/2
        # self.mean_value = sum(self.values)/len_values #TODO: See if numpy.mean is faster
        self.probability = 1.0/len_values

        # Assert that the probability sum is close to 1.0
        probability_sum = self.probability * len_values
        assert isclose(1.0, probability_sum)

        # TODO:Define separate probabilities, probabilities are currently equal
        # Loop through every face and sum the probabilities

        # TODO:All dice are the same, add UIDs to track individual dice

    def roll(self, num_rolls=1):
        """Roll N dice and return a list of values."""
        # Check Die
        if not self.values:
            raise ValueError('Values must not be empty in order to Die.roll().')

        # Roll <num_rolls> times
        rolls = [randint(0, len(self.values)-1) for i in range(num_rolls)]
        return [self.values[i] for i in rolls]

    def min(self, num_rolls=1):
        """Minimum value of N dice rolls."""
        return num_rolls * self._min_value

    def max(self, num_rolls=1):
        """Maximum value of N dice rolls."""
        return num_rolls * self._max_value

    def mean(self, num_rolls=1):
        """Mean value of N dice rolls."""
        return num_rolls * self._mean_value


# Self-test
if __name__ == '__main__':
    print('Testing dice.py...')

    print('\tTesting Die construction', end='...')

    # No input
    try:
        TEST_DIE = Die()
    except TypeError:
        pass

    # Double input
    try:
        TEST_DIE = Die(4.0)
    except TypeError:
        pass

    # Negative input
    try:
        TEST_DIE = Die(-4)
    except ValueError:
        pass

    # Real input for 1d0
    TEST_D0 = Die(0)
    assert TEST_D0.max() == 0
    assert TEST_D0.max() == 0
    assert isclose(0.0, TEST_D0.mean())
    assert isclose(1.0, TEST_D0.probability)

    # Real input for 1d20
    TEST_D20 = Die(20)
    assert TEST_D20.max() == 20
    assert TEST_D20.min() == 1
    assert isclose(10.5, TEST_D20.mean())
    assert isclose(1.0/TEST_D20.max(), TEST_D20.probability)

    print('PASSED')

    print('\tTest Die rolls', end='...')

    # Test die roll
    TEST_ROLL = TEST_D20.roll()
    assert isinstance(TEST_ROLL, list)
    assert TEST_ROLL[0] >= TEST_D20.min()
    assert TEST_ROLL[0] <= TEST_D20.max()
    assert TEST_ROLL[0] in TEST_D20.values
    print(TEST_ROLL[0], end='...')

    # Test no roll
    TEST_ROLL = TEST_D20.roll(0)
    assert isinstance(TEST_ROLL, list)
    assert not TEST_ROLL

    # Test multiple rolls
    TEST_ROLL = TEST_D20.roll(3)
    assert isinstance(TEST_ROLL, list)
    for i in enumerate(TEST_ROLL):
        print(TEST_ROLL[i[0]], end='...')

    print('PASSED')

    print('dice.py PASSED')
