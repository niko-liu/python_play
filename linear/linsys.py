from decimal import Decimal, getcontext
from copy import deepcopy

from nkpy2.vector import Vector
from linear.plane import Plane

getcontext().prec = 30


class LinearSystem(object):
    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        tmp_p1 = self.planes[row1]
        tmp_p2 = self.planes[row2]
        self.planes[row1] = tmp_p2
        self.planes[row2] = tmp_p1

    def multiply_coefficient_and_row(self, coefficient, row):
        plane_selected = self.planes[row]
        plane_selected.normal_vector = plane_selected.normal_vector.__mul__(coefficient)
        new_constant_term = plane_selected.constant_term * coefficient
        plane_selected.constant_term = new_constant_term

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        plane_to_add = self.planes[row_to_add]
        v_tmp = plane_to_add.normal_vector.__mul__(coefficient)
        tmp_constant_term = plane_to_add.constant_term * coefficient
        plane_be_added = self.planes[row_to_be_added_to]
        plane_be_added.normal_vector = plane_be_added.normal_vector.__add__(v_tmp)
        plane_be_added.constant_term += tmp_constant_term

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i + 1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


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
