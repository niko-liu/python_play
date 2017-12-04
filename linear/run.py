# encoding: utf-8

from linear.line import Line
from nkpy2.vector import Vector


l1 = Line(normal_vector=Vector([4.046, 2.836]), constant_term=1.21)
l2 = Line(normal_vector=Vector([10.115, 7.09]), constant_term=3.025)
print(l1.__str__(), " ", l2.__str__())
print(l1.intersection(l2))
print(l1.basepoint)
print(l2.basepoint)
print(l1.is_parallel_to(l2))
print(l1.is_same_line(l2))

l3 = Line(normal_vector=Vector([7.204, 3.182]), constant_term=8.68)
l4 = Line(normal_vector=Vector([8.172, 4.114]), constant_term=9.883)
print(l3.__str__(), " ", l4.__str__())
print(l3.intersection(l4))
print(l3.basepoint)
print(l4.basepoint)
print(l3.is_parallel_to(l4))
print(l3.is_same_line(l4))


l5 = Line(normal_vector=Vector([1.182, 5.562]), constant_term=6.744)
l6 = Line(normal_vector=Vector([1.773, 8.343]), constant_term=9.525)
print(l5.basepoint)
print(l6.basepoint)
print(l5.__str__(), " ", l6.__str__())
print(l5.intersection(l6))
print(l5.is_parallel_to(l6))
print(l5.is_same_line(l6))

