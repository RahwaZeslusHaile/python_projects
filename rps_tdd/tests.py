
from unittest import TestCase


from unittest import TestCase


class RpsTests(TestCase):

    def test_rock_vs_scissors_left_wins(self):
        left = "rock"
        right = "scissors"

        result = rps(left, right)
        self.assertEqual(result, "left")

    def test_scissors_vs_rock_right_wins(self):
            left = "scissors"
            right = "rock"

            result = rps(left, right)

            self.assertEqual(result, "right")

def rps(left,right):
    return "left" if left =="rock" else "right"
    