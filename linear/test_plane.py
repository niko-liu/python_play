# encoding: utf-8

from plane import Plane
from vector import Vector


p1 = Plane(Vector([-0.142, 3.806, 0.728]), -3.46)
p2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)
print(p1.__str__(), " ", p2.__str__())
print(p1.is_parallel_to(p2))
print(p1.is_same_plane(p2))

p1 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
p2 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)
print(p1.__str__(), " ", p2.__str__())
print(p1.is_parallel_to(p2))
print(p1.is_same_plane(p2))

p1 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
p2 = Plane(Vector([-2.642, 2.875, -2.404]), 2.443)
print(p1.__str__(), " ", p2.__str__())
print(p1.is_parallel_to(p2))
print(p1.is_same_plane(p2))
