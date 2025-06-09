
# module9_knn_gridsearchcv.py

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# 获取训练集数据
N = int(input("Enter the number of training samples (N): "))
train_X = []
train_y = []

print("Enter the training data pairs (x y):")
for _ in range(N):
    x = float(input("  x: "))
    y = int(input("  y: "))
    train_X.append(x)
    train_y.append(y)

train_X = np.array(train_X).reshape(-1, 1)
train_y = np.array(train_y)

# 获取测试集数据
M = int(input("Enter the number of test samples (M): "))
test_X = []
test_y = []

print("Enter the test data pairs (x y):")
for _ in range(M):
    x = float(input("  x: "))
    y = int(input("  y: "))
    test_X.append(x)
    test_y.append(y)

test_X = np.array(test_X).reshape(-1, 1)
test_y = np.array(test_y)

# 建立kNN模型 + GridSearchCV超参数搜索
param_grid = {'n_neighbors': list(range(1, 11))}
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=3)
grid_search.fit(train_X, train_y)

# 用最佳k进行测试集预测
best_k = grid_search.best_params_['n_neighbors']
best_model = grid_search.best_estimator_
pred_y = best_model.predict(test_X)

# 输出结果
accuracy = accuracy_score(test_y, pred_y)
print(f"\nBest k found: {best_k}")
print(f"Test set accuracy: {accuracy:.4f}")
