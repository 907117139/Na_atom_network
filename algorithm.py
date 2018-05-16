import interpolation

def compute_parameter(lambda1, lambda2):
    wave_number1 = interpolation.convert_to_wave_number(lambda1)
    wave_number2 = interpolation.convert_to_wave_number(lambda2)
    energy_level1 = interpolation.find_energy_level(lambda1)
    energy_level2 = interpolation.find_energy_level(lambda2)

    n = interpolation.find_n(lambda1, lambda2)
    delta = round(abs(wave_number1 - wave_number2), 3)
    col = interpolation.find_which_col(delta)
    alpha = interpolation.find_alpha(delta, col)
    m = interpolation.find_m(col)
    delta_l = interpolation.find_delta_l(n, m, alpha)

    lambda_max = max(lambda1, lambda2)
    wave_number = interpolation.convert_to_wave_number(lambda_max)
    R = interpolation.R
    fixed_term = interpolation.find_fixed_term(wave_number, R, n, delta_l)

    return {'wave_number1': wave_number1, 'wave_number2': wave_number2,'energy_level1': energy_level1,
            'energy_level2': energy_level2, 'fixed_term': fixed_term, 'delta': delta, 'n': n, 'delta_l': delta_l}