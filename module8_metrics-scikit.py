
import numpy as np
from sklearn.metrics import precision_score, recall_score

# Ask user for number of data points
N = int(input("Enter the number of data points (N): "))

# Initialize lists to store ground truth (X) and predictions (Y)
x_true = []
y_pred = []

# Collect N (x, y) points from the user
print("Enter each pair of (x, y):")
for i in range(N):
    x = int(input(f"Point {i+1} - Enter true class (0 or 1): "))
    y = int(input(f"Point {i+1} - Enter predicted class (0 or 1): "))
    x_true.append(x)
    y_pred.append(y)

# Convert to numpy arrays
x_true = np.array(x_true)
y_pred = np.array(y_pred)

# Calculate metrics
precision = precision_score(x_true, y_pred)
recall = recall_score(x_true, y_pred)

# Output the results
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
