import numpy as np
X = np.array([[-2, 1], [3, 1], [3, 1], [7, 1], [9, 1]])
y = np.array([0, 4, 5, 8, 10])

# Arbitrary point / Произвольная точка.
x_pre = 7

# w - vector of coefficients [k, m] / w — вектор коэффициентов [k, m].
w = np.linalg.inv(X.T @ X) @ X.T @ y

# Prediction for an arbitrary point by the formula of a straight line / Предсказание для произвольной точки по формуле прямой.
result = w[0] * x_pre + w[1]
print(result)