# encoding: utf-8

from linear.linsys import LinearSystem
from linear.plane import Plane
from nkpy2.vector import Vector

# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2):
#     print('test case 1 failed')
#
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print('test case 2 failed')
# print(s.cal_result(t))
#
# print('\nsystem in 4\n')
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
# s = LinearSystem([p1, p2, p3, p4])
# t = s.compute_triangular_form()
# for t_t in t:
#     print(t_t)
#
# if not (t[0] == p1 and
#         t[1] == p2 and
#         t[2] == Plane(normal_vector=Vector(['0', '0', '-2']), constant_term='2') and
#         t[3] == Plane()):
#     print('test case 3 failed')
# print(s.cal_result(t))
#
# print('\n')
#
# p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
# s = LinearSystem([p1, p2, p3])
# t = s.compute_triangular_form()
# for t_t in t:
#     print(t_t)
# if not (t[0] == Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0', '0', '-9']), constant_term='-2')):
#     print('test case 4 failed')
# print(s.cal_result(t))

p1 = Plane(normal_vector=Vector(['5.862', '1.178', '-10.366']), constant_term='-8.15')
p2 = Plane(normal_vector=Vector(['-2.931', '-0.589', '5.183']), constant_term='-4.075')
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
for t_t in t:
    print(t_t)
print(s.cal_result(t))

print("\n")

p1 = Plane(normal_vector=Vector(['8.631', '5.112', '-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=Vector(['4.315', '11.132', '-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=Vector(['-2.158', '3.01', '-1.727']), constant_term='-0.831')
s = LinearSystem([p1, p2, p3])
t = s.compute_triangular_form()
for t_t in t:
    print(t_t)
print(s.cal_result(t))

print("\n")

p1 = Plane(normal_vector=Vector(['5.262', '2.739', '-9.878']), constant_term='-3.441')
p2 = Plane(normal_vector=Vector(['5.111', '6.358', '7.63']), constant_term='-2.152')
p3 = Plane(normal_vector=Vector(['2.016', '-9.924', '-1.367']), constant_term='-9.278')
p4 = Plane(normal_vector=Vector(['2.167', '-13.543', '-18.883']), constant_term='-10.567')
s = LinearSystem([p1, p2, p3, p4])
t = s.compute_triangular_form()
for t_t in t:
    print(t_t)
print(s.cal_result(t))
