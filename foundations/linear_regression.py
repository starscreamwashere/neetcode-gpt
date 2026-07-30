import numpy as np
from numpy.typing import NDArray

class Solution:
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # Matrix multiplication / dot product of X and weights
        predictions = np.matmul(X, weights)
        
        # Round the resulting array to 5 decimal places
        return np.round(predictions, 5)

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute Mean Squared Error (MSE)
        mse = np.mean((model_prediction - ground_truth) ** 2)
        
        # Round the scalar float result to 5 decimal places
        return float(np.round(mse, 5))