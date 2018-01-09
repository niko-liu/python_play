# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x_arr = np.array([0, 1, 2, 3])
y_arr = np.array([2, 1, 1, 2])
#
# print("x_arr**4={}".format((x_arr**4).sum()))
# print("x_arr**3={}".format((x_arr**3).sum()))
# print("x_arr**2={}".format((x_arr**2).sum()))
# print("x_arr={}".format(x_arr.sum()))
# print("\n")
# print("y_arr={}".format(y_arr.sum()))
# print("xy={}".format((x_arr * y_arr).sum()))
# print("x^2y={}".format(((x_arr**2) * y_arr).sum()))


arr_a = [[196, 72, 28],
         [72, 28, 12],
         [14, 6, 4]]
matrix_b = np.array([[48], [18], [6]])
matrix_A = np.array(arr_a)
matrix_abc = np.linalg.inv(matrix_A).dot(matrix_b)

print(matrix_abc)
matrix_t = np.transpose(matrix_abc).round(2)
print(matrix_t)

X = np.linspace(-0.5, 3.5, num=1000)
Y = matrix_t[0][0]*(X**2) + matrix_t[0][1]*X + matrix_t[0][2]

plt.figure()
plt.title("$f(x)=({})x^2+({})x+({})$".format(matrix_t[0][0], matrix_t[0][1], matrix_t[0][2]))
plt.scatter(x_arr, y_arr, c='r')
plt.plot(X, Y)
plt.show()
