from python.sampler import sample_breakout_u, sample_breakout_n
from python.expansion_temp import coefficients_4d
from python import interpolation_experiment
import numpy as np

def rmse(list1, list2):
    return np.mean(np.sqrt((list1-list2)**2))

ob = coefficients_4d()
M=0
order = 2
err = 10
tol = 1e-4
ob.make_drive_coefficients_he(M, order)
coeffs_old = ob.c_He_drive
order_list = [2,4,6,8,10]
it = 1
while err > tol:
    order = order_list[it]
    print(order, 'order')
    ob.make_drive_coefficients_he(M, order)
    coeffs_new = ob.c_He_drive
    err = rmse(coeffs_new, coeffs_old)
    print(err, 'RMSE')
    coeffs_old = coeffs_new
    ob.save_he_drive()
    it += 1


