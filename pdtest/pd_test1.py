# encoding: utf-8

import pandas as pd

s1 = pd.Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series(data=[10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
print(s1+s2)
print("\n")
s3 = s1.add(s2, fill_value=0)
print(s3.dropna())
print("\n")
print(s3)
print("\n")
print(s1)
