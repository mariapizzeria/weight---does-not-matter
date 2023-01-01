# The same thing only with massive data / Тоже самое только с массивными данными.
import numpy as np

X = np.array(
    [
        [ 3,  2,  1],
        [ 3, -5,  1], 
        [ 0, -3,  1],
        [ 2, -5,  1],
        [-3, -6,  1],
        [-4, -2,  1]
	]
)

y = np.array(
	[
        0.89652141, 
        3.24215720, 
        4.00879645, 
        7.12548724, 
        7.89652144,
        9.68552258
	]
)

x_pre = [2, -3, 1]
w = np.linalg.inv(X.T @ X) @ X.T @ y

result = x_pre @ w
print(w) # Received weights / Полученные веса.
print(result) # Predictions for the X_pre point / Предсказания для точки X_pre.