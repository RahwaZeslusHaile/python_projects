
from unittest import TestCase


from unittest import TestCase


class RpsTests(TestCase):

    def test_rock_vs_scissors_left_wins(self):
        left = "rock"
        right = "scissors"

        result = rps(left, right)
        print(result)

        self.assertEqual(result, "left")

def rps(left,right):
    return "left"