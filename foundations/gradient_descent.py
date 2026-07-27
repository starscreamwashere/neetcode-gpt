class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        y2=2*init
        x_old=init
        x_new=x_old
        while(iterations>0):
            x_new=x_old-learning_rate*y2
            x_old=x_new
            y2=2*x_new
            iterations=iterations-1
        x_new=round(x_new,5)
        return x_new

