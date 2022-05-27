import math

year = 2022
month = 5
day = 7

east = 15.971389

cet = 22.25
gmt = cet - 1

j_0 = 367.0 * year - math.floor((7.0 * (year + math.floor((month+9.0)/12.0)))/4.0) + math.floor(275.0*month/9.0) + day + 1721013.5
print('j_0: {}'.format(j_0))
j_d = j_0 + gmt / 24
print('j_d: {}'.format(j_d))

t_0 = (j_0 - 2451545) / 36525
print('t_0: {}'.format(t_0))
theta_g_0 = 100.4606184 + 36000.77004 * t_0 + 0.000387933 * math.pow(t_0, 2) - 2.583 * math.pow(10, -8) * math.pow(t_0, 3)
theta_g_0 -= 360.0 * math.floor(theta_g_0 / 360.0)
print('theta_g_0: {}'.format(theta_g_0))

theta_g = theta_g_0 + 0.00417807 * (gmt / 24) * 24 * 3600 - 360 * math.floor(theta_g_0 / 360.0)
theta_g -= 360.0 * math.floor(theta_g / 360.0)
print('theta_g: {}'.format(theta_g))

theta_zg = theta_g + east
print('theta_zg: {}'.format(theta_zg))
