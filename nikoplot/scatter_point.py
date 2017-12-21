# encoding: utf-8


import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


rand_size = 300


def calculate_mb(X, Y):
    n = rand_size
    sum_X = sum(X)
    sum_Y = sum(Y)
    X_bar = sum_X / n
    Y_bar = sum_Y / n
    squart_X = sum([x*y for x, y in zip(X, X)])
    sum_XY = sum([x * y for x, y in zip(X, Y)])
    m = (n * sum_XY - sum_X * sum_Y) / (n * squart_X - sum_X**2)
    b = Y_bar - m * X_bar
    print("m=%s, b=%s" % (m, b))
    return m, b


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
test_m = random.randint(-10, 10)
X = np.random.randn(rand_size)
Y = np.zeros(rand_size)
print("test_m = %s" % test_m)
for i in range(rand_size):
    Y_min = test_m * X[i] + 2 - random.uniform(-10, 20)
    Y_max = test_m * X[i] + 4 + random.uniform(-5, 5)
    Y[i] = random.uniform(Y_min, Y_max)

vector_mb = calculate_matrix(X, Y)
m, b = calculate_mb(X, Y)
line_Y = vector_mb[0] * X + vector_mb[1]
fig, ax = plt.subplots()
ax.scatter(X[0:], Y[0:], alpha=0.5)
ax.set_xlabel(r'X', fontsize=15)
ax.set_ylabel(r'Y', fontsize=15)
ax.set_title('points plot')
ax.add_line(Line2D(X, line_Y, linewidth=1, color='red'))
ax.grid(True)
fig.tight_layout()
plt.show()
