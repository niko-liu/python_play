# encoding: utf-8

from linear.line import Line
from nkpy2.vector import Vector
from linear.plane import Plane
from linear.linsys import LinearSystem, MyDecimal


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

p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

s = LinearSystem([p0, p1, p2, p3])

print(s.indices_of_first_nonzero_terms_in_each_row())
print('{},{},{},{}'.format(s[0], s[1], s[2], s[3]))
print(len(s))
print(s)

s[0] = p1
print(s)

print(MyDecimal('1e-9').is_near_zero())
print(MyDecimal('1e-11').is_near_zero())

s = LinearSystem([p0, p1, p2, p3])
s.swap_rows(0, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 1 failed')

s.swap_rows(1, 3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print('test case 2 failed')

s.swap_rows(3, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 3 failed')

s.multiply_coefficient_and_row(1, 0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print('test case 4 failed')

s.multiply_coefficient_and_row(-1, 2)
print("test5 s2=", s[2])
if not (s[0] == p1 and
        s[1] == p0 and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print('test case 5 failed\n')

s.multiply_coefficient_and_row(10, 1)
print("test6 s1", s[1])
print("test6 s2=", s[2])
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print('test case 6 failed\n')

s.add_multiple_times_row_to_row(0, 0, 1)
print("test7 s1", s[1])
print("test7 s2=", s[2])
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print('test case 7 failed\n')

s.add_multiple_times_row_to_row(1, 0, 1)
print("test8 s1=", s[1], "\ns2=", s[2])
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print('test case 8 failed\n')

s.add_multiple_times_row_to_row(-1, 1, 0)
print("test9 s0=", s[0], "\ns1=", s[1], "\ns2=", s[2])
if not (s[0] == Plane(normal_vector=Vector(['-10', '-10', '-10']), constant_term='-10') and
        s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print('test case 9 failed\n')
