# Link: https://neetcode.io/problems/gradient-descent

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for i in range(iterations):
            der = 2 * x
            x -= der * learning_rate
        return round(x, 5)