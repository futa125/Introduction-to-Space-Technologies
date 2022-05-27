import numpy as np
from scipy.optimize import fsolve

mi = 398600
earth_radius = 6371.0 # km
time_elapsed = 208.3 # min

r_vector = np.array([27002.1, 28469.3, -6836.6])
v_vector = np.array([-1.01, 1.90, 0.62])

r = np.linalg.norm(r_vector)

v = np.linalg.norm(v_vector)

v_r = np.dot(r, v) / r
print('v_r: {}'.format(v_r))

# a)
h_vector = np.cross(r_vector, v_vector)
h = np.linalg.norm(h_vector)
print('h: {}'.format(h))

e_vector = (1 / mi) * (np.cross(v_vector, h_vector) - mi * (r_vector / r))
e = np.linalg.norm(e_vector)
print('e: {}'.format(e))

k_vector = np.array([0, 0, 1])
n_vector = np.cross(k_vector, h_vector)
n = np.linalg.norm(n_vector)
print('n: {}'.format(np.degrees(n)))
print('n_y: {}'.format(n_vector[1]))
uppercase_omega = np.arccos(n_vector[0] / n) # n_y >= 0
print('uppercase omega: {}'.format(np.degrees(uppercase_omega)))

print('e_z: {}'.format(e_vector[2]))
lowercase_omega = np.arccos(np.dot(n_vector, e_vector) / (n * e)) # e_z >= 0
print('lowercase omega: {}'.format(np.degrees(lowercase_omega)))

i = np.arccos(h_vector[2] / h)
print('i: {}'.format(np.degrees(i)))

theta = np.arccos(np.dot(e_vector, r_vector) / (e * r))
print('theta: {}'.format(np.degrees(theta)))
print()


# b)
perigee = (h * h) / (mi * (1 + e))
print('perigee: {}'.format(perigee))
z_min = perigee - earth_radius
print('z_min: {}'.format(z_min))
apogee = (h*h) / (mi * (1 - e))
print('apogee: {}'.format(apogee))
z_max = apogee
print('z_max: {}'.format(z_max))
print()


# c)
a = (h ** 2 / mi) * (1 / (1 - e ** 2))
print('a: {}'.format(a))
t = 2 * np.pi * np.sqrt(a ** 3 / mi)
print('t: {}'.format(t))

e_0 = 2 * np.arctan(np.sqrt((1 - e) / (1 + e)) * np.tan(theta / 2))
print('e_0: {}'.format(e_0))
m_0 = e_0 - e * np.sin(e_0)
print('m_0: {}'.format(m_0))
t_0 = m_0 * t / (2 * np.pi)
print('t_0: {}'.format(t_0))
t_after = t_0 + time_elapsed * 60
print('t_after: {}'.format(t_after))
m_after = 2 * np.pi * (t_after / t)
print('m_after: {}'.format(m_after))


def e_after_func(x):
    return x[0] - e * np.sin(x[0]) - m_after


e_after = fsolve(e_after_func, np.array([1]))[0]
print('e_after: {}'.format(e_after))
theta_after = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(e_after / 2))
print('theta_after: {}'.format(np.degrees(theta_after) + 360))
