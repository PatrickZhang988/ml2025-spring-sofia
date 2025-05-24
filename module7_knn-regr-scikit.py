# module7_knn-regr-scikit.py

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Step 1: Read input N and k
try:
    N = int(input("Enter number of data points (N): "))
    k = int(input("Enter number of nearest neighbors (k): "))

    if N <= 0 or k <= 0:
        raise ValueError("N and k must be positive integers.")

    if k > N:
        raise ValueError("k cannot be greater than N.")

except ValueError as e:
    print("Input error:", e)
    exit()

# Step 2: Read N (x, y) points
x_values = []
y_values = []

print(f"\nEnter {N} data points:")
for i in range(N):
    x = float(input(f"  Enter x value for point {i+1}: "))
    y = float(input(f"  Enter y value for point {i+1}: "))
    x_values.append(x)
    y_values.append(y)

# Step 3: Convert to numpy arrays
X = np.array(x_values).reshape(-1, 1)
y = np.array(y_values)

# Step 4: Show variance of labels
label_variance = np.var(y)
print(f"\nVariance of labels in the training dataset: {label_variance:.4f}")

# Step 5: Fit k-NN regression model
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X, y)

# Step 6: Get input X for prediction
try:
    query = float(input("\nEnter X value for prediction: "))
    prediction = model.predict(np.array([[query]]))
    print(f"Predicted Y value for X = {query} is: {prediction[0]:.4f}")
except Exception as e:
    print("Prediction error:", e)
