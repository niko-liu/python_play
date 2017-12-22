# encoding: utf-8


import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

rand_size = 300


# 根据方差计算最大似然估计直线
def calculate_mb(X, Y):
    n = rand_size
    sum_X = sum(X)
    sum_Y = sum(Y)
    X_bar = sum_X / n
    Y_bar = sum_Y / n
    squart_X = sum([x * y for x, y in zip(X, X)])
    sum_XY = sum([x * y for x, y in zip(X, Y)])
    m = (sum_XY - sum_X * Y_bar) / (squart_X - sum_X * X_bar)
    b = Y_bar - m * X_bar
    print("m=%s, b=%s" % (m, b))
    return m, b


# 根据A^TAx=A^Tb，估计x法向量
def calculate_matrix(X, Y):
    matrix_x = np.zeros((rand_size, 2))
    for i in range(rand_size):
        matrix_x[i][0] = X[i]
        matrix_x[i][1] = 1
    transpost_x = np.transpose(matrix_x)
    transpost_y = np.transpose(Y)
    print("trans_x * transpost_y =", np.dot(transpost_x, transpost_y))
    print("trans_x * matrix =", np.dot(transpost_x, matrix_x))
    vector_mb = np.dot(np.linalg.inv(np.dot(transpost_x, matrix_x)), np.dot(transpost_x, transpost_y))
    print("vector_mb = ", vector_mb)
    return vector_mb


np.random.seed(9999)
test_m = random.randint(-10, 10)  # 随机抽取一个直线斜率
X = np.random.randn(rand_size)  # 随机生成x坐标数组
Y = np.zeros(rand_size)
print("test_m = %s" % test_m)
# 控制散点生成，控制Y坐标随机散点
for i in range(rand_size):
    Y_min = test_m * X[i] + 2 - random.uniform(-1, 2)
    Y_max = test_m * X[i] + 4 + random.uniform(-1, 2)
    Y[i] = random.uniform(Y_min, Y_max)
# 通过线性方程计算回归方程
vector_mb = calculate_matrix(X, Y)

# 通过求导方式计算回归方程
m, b = calculate_mb(X, Y)

# 构建直线
line_Y = vector_mb[0] * X + vector_mb[1]

fig, axes = plt.subplots(2)
axes[0].scatter(X[0:], Y[0:], alpha=0.5)
axes[0].set_xlabel(r'X', fontsize=15)
axes[0].set_ylabel(r'Y', fontsize=15)
axes[0].set_title('points plot') # 构建散点图

# 画一条直线
axes[0].add_line(Line2D(X, line_Y, linewidth=1, color='red'))
axes[0].grid(True)

axes[1].boxplot(line_Y, labels=['Y'])
axes[1].set_title(r'Y range')

fig.tight_layout()
plt.show()
