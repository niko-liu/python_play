# encoding: utf-8

import math


class Vector(object):
    """
    向量模块
    """

    def __init__(self, coordinates):
        """
        构造
        :param coordinates: 坐标（列表）
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)  # 坐标
            self.dimension = len(coordinates)  # 维度

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def multiple_vector(self, times):
        v_new = []
        for i in range(len(self.coordinates)):
            v1_c = self.coordinates[i]
            v_new.append((v1_c * times))
        return Vector(v_new)

    def sum_vector(self, v2):
        v_new = []
        for i in range(len(self.coordinates)):
            v1_c = self.coordinates[i]
            v2_c = v2.coordinates[i]
            v_new.append((v1_c + v2_c))

        return Vector(v_new)

    def minus_vector(self, v2):
        """
        v2 - v1
        :param v2:
        :return:
        """
        v_new = []
        for i in range(len(self.coordinates)):
            v1_c = self.coordinates[i]
            v2_c = v2.coordinates[i]
            v_new.append((v1_c - v2_c))

        return Vector(v_new)

    def cal_magnitube(self):
        vc2 = [pow(self.coordinates[i], 2) for i in range(len(self.coordinates))]
        vsum = sum(vc2)
        return math.sqrt(vsum)

    def normalization(self):
        try:
            vmagnitube = self.cal_magnitube()
            u_vector = [self.coordinates[i] / vmagnitube for i in range(len(self.coordinates))]
            return u_vector
        except ValueError:
            print("value error!!!")

    def inner_product(self, v2):
        inner_product = 0
        for i in range(len(self.coordinates)):
            inner_product += self.coordinates[i] * v2.coordinates[i]
        return inner_product

    def dot(self, v2):
        xysum = sum([x * y for x, y in zip(self.coordinates, v2.coordinates)])
        return round(xysum, 3)

    def rad(self, v2):
        try:
            vu1 = Vector(self.normalization())
            vu2 = Vector(v2.normalization())
            r = round(math.acos(vu1.dot(vu2)), 3)
            # print(r)
            return r
        except ValueError:
            print("zero-vector can not be calculated!!!!")

    def degrees(self, v2):
        rad = self.rad(v2)
        return math.degrees(rad)

    def is_parallel_to(self, v2):
        return (self.is_zero() or v2.is_zero()
                or self.rad(v2) == 0 or
                self.rad(v2) == round(math.pi, 3))

    def is_orthogronal_to(self, v2):
        return (self.is_zero() or v2.is_zero()
                or self.rad(v2) == round(math.pi / 2, 3))

    def is_zero(self, tolerance=1e-10):
        return self.cal_magnitube() < tolerance

    def degrees2(self, v2):
        rad = self.rad(v2)
        degrees_per_rad = 180 / math.pi
        return round(degrees_per_rad * rad)

    def projection(self, v2):
        uv2 = Vector(v2.normalization())
        projv_len = self.dot(uv2)
        return uv2.multiple_vector(projv_len)

    def vper(self, v2):
        projv = self.projection(v2)
        return self.minus_vector(projv)

    def cross_products(self, v2):
        cross_v = []
        if self.dimension == 3:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v2.coordinates
            cross_v = [(y_1 * z_2 - y_2 * z_1),
                       (x_2*z_1 - x_1 * z_2),
                       (x_1 * y_2 - x_2 * y_1)]
        if self.dimension == 2:
            cross_v = [0, 0]
        return Vector(cross_v)

    def area_cross_products(self, v2):
        cv = self.cross_products(v2)
        print(cv)
        return cv.cal_magnitube()
