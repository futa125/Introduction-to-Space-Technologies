import numpy as np

# Initial data
a = 0.1
conductor_length = 190
N = conductor_length / (4 * a)
current = 111 * (10 ** -3)
r = 0.14 * (10 ** -3)
print('a = {}'.format(a))
print('conductor_length = {}'.format(conductor_length))
print('N = {}'.format(N))
print('current = {}'.format(current))
print('r = {}'.format(r))

# 2
m_magnitude = np.sqrt(2) * N * current * (a ** 2)
print('|m| = {} Am^2'.format(m_magnitude))
print()

# 3
B = 38 * (10 ** -6)
print('B = {}'.format(B))
tau_magnitude = N * current * (a ** 2) * B  # * np.sin(90 degrees) == 1
print('|tau| = {} Nm'.format(tau_magnitude))
print()

# 4
S = (r ** 2) * np.pi
resistance = 1.68 * (10 ** -8)
print('S = {}'.format(S))
print('resistance = {}'.format(resistance))
R = resistance * conductor_length / S
print('R = {} Ohm'.format(R))
print()

# 5
P = (current ** 2) * R
print('P = {} W'.format(P))
print()

# 6
satellite_mass = 1
satellite_size = 0.1
print('satellite_mass = {}'.format(satellite_mass))
print('satellite_size = {}'.format(satellite_size))
satellite_I = satellite_mass * (satellite_size ** 2) / 6
print('I = {} kgm^2'.format(satellite_I))
print()

# 7
omega = np.radians(19)
M = (10 ** -5)
alpha = M / satellite_I
t = omega / alpha
print('omega = {}'.format(omega))
print('alpha = {}'.format(alpha))
print('M = {}'.format(M))
print('t = {} s'.format(t))
print()
