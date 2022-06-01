from statistics import NormalDist

H = 404  # km
height_at_average_value = 400  # km
standard_deviation = 100  # km

TEC_S1 = 38  # TECU
TEC_S2 = 36  # TECU
TEC_S3 = 35  # TECU
TEC_S4 = 45  # TECU

delta_x = 300  # km
delta_y = 165  # km

x_min = 1185  # km
x_max = 1580  # km
y_min = 4995  # km
y_max = 5550  # km

frequency = 1176.45 * 10**6  # Hz

# a)

# P(X > x) = 1 - P(X <= x) = 1 - CDF(N(400, 100^2), x)
# x -> Visina ISS2 iznad Zemljine površine -> 404 km

# N -> Normalna (Gaussova) razdioba sa srednjom vrijednošću 400 km i standardnom devijacijom 100 km
# CDF -> Kumulativna funkcija distribucija -> P(X <= x), za x iz skupa realnih brojeva

norm_dist = NormalDist(mu=height_at_average_value, sigma=standard_deviation)
electron_content_percentage_above_ISS2 = 1 - norm_dist.cdf(H)
print("Postotak ukupnog sadržaja elektrona u ionosferi koji se nalazi iznad ISS2: {:.4f} %"
      .format(electron_content_percentage_above_ISS2 * 100))

# b)
x_p = x_min + delta_x  # km
y_p = y_min + delta_y  # km
print("Koordinate točke P: {} km, {} km".format(x_p, y_p))

# c)
x_p_norm = (x_p - x_min) / (x_max - x_min)
y_p_norm = (y_p - y_min) / (y_max - y_min)

TEC = TEC_S1 * x_p_norm * y_p_norm + \
      TEC_S2 * (1 - x_p_norm) * y_p_norm + \
      TEC_S3 * (1 - x_p_norm) * (1 - y_p_norm) + \
      TEC_S4 * x_p_norm * (1 - y_p_norm)
print("Ukupni sadržaj elektrona u ionosferi izračunat za lokaciju P korištenjem "
      "ionosferskog modela sustava EGNOS: {:.4f} TECU".format(TEC))

# d)
# delta_I_T = (40.3 / (f^2 * c)) * 10^16
# delta_I_T_P = (40.3 / (f^2 * c)) * TEC * 10^16
delta_I_T_P = 40.3 / (frequency**2 * 3 * 10 ** 8) * TEC * 10 ** 16  # s
print("Ionosfersko kašnjenje na lokaciji P (izračunato EGNOS-om) n"
      "a frekvenciji od f=1176.45 MHz: {:.4f} ns".format(delta_I_T_P * 10 ** 9))

# e)
delta_I_T_ISS2 = delta_I_T_P * electron_content_percentage_above_ISS2  # s
print("Ionosfersko kašnjenje signala s Galileo satelita "
      "koji se nalazi u zenitnom smjeru iznad ISS2: {:.4f} ns".format(delta_I_T_ISS2 * 10 ** 9))

# f)
# delta_I_S_ISS2 = delta_I_T_ISS2 * c
delta_I_S_ISS2 = delta_I_T_ISS2 * 3 * 10 ** 8  # m
print("Pogreška procijenjene udaljenosti od tog Galileo satelita "
      "do ISS2 kada ju ne bismo kompenzirali: {:.4f} m".format(delta_I_S_ISS2))
