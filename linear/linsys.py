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

    def compute_triangular_form(self):
        system = deepcopy(self)
        # self.order_equations(system)
        system.planes = self.gaussian_elimination(system)
        self.order_equations(system)
        print("===============")
        for p_p in system.planes:
            print(p_p)
        print("===============")

        return system.planes

    @staticmethod
    def order_equations(system):
        for i in range(len(system.planes)):
            dimension = system.planes[i].normal_vector.dimension
            coord1 = system.planes[i].normal_vector.coordinates
            for j in range(i+1, len(system.planes)):
                dimension2 = system.planes[j].normal_vector.dimension
                coord2 = system.planes[j].normal_vector.coordinates
                if dimension < dimension2:
                    system.swap_rows(i, j)
                    break
                else:
                    count_zero_1 = 0
                    count_zero_2 = 0
                    for k in range(dimension):
                        if coord1[k] == 0:
                            count_zero_1 += 1
                        if coord2[k] == 0:
                            count_zero_2 += 1
                    if count_zero_1 > count_zero_2:
                        system.swap_rows(i, j)
                        break
        return system.planes

    @staticmethod
    def gaussian_elimination(system):
        plen = len(system.planes)
        x_nonzero_idx = 0
        for i in range(plen):
            if system.planes[i].normal_vector.coordinates[0] != 0:
                x_nonzero_idx = i
                break
        if x_nonzero_idx != 0:
            system.swap_rows(0, x_nonzero_idx)

        for i in range(plen):
            plane = system.planes[i]
            for j in range(i+1, plen):
                plane2 = system.planes[j]
                if plane.normal_vector.coordinates[i] == 0:
                    break
                grammer = plane2.normal_vector.coordinates[i]
                alpha = grammer / plane.normal_vector.coordinates[i]
                plane2.normal_vector = plane2.normal_vector.__sub__(plane.normal_vector.__mul__(alpha))
                plane2.constant_term = plane2.constant_term - (plane.constant_term * alpha)
                system.planes[j] = plane2
        return system.planes


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
