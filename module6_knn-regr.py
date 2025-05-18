# module6_knn-regr.py

import numpy as np

N = int(input("Enter number of data points (N): "))
k = int(input("Enter number of nearest neighbors (k): "))

x_values = []
y_values = []

for i in range(N):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    x_values.append(x)
    y_values.append(y)

x_array = np.array(x_values)
y_array = np.array(y_values)

query_x = float(input("Enter the X value to predict Y for: "))

if k > N:
    print("Error: k cannot be greater than the number of data points.")
else:
    distances = np.abs(x_array - query_x)
    nearest_indices = np.argsort(distances)[:k]
    predicted_y = np.mean(y_array[nearest_indices])
    print(f"Predicted Y value: {predicted_y}")
