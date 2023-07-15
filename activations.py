import numpy as np
import csv

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1 - np.tanh(x) ** 2


def poly(x):
    return_value = []
    for x_value in x:
        if x_value < -2.0:
            return -1.0
        elif x_value > 2.0:
            return 1.0
        else:
            x_float = float(x_value)
            coeffs = []
            with open('poly.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    # print(str(row[0]))
                    coeffs.append(float(row[0]))

                polynominal_value = 0

                for i in range(len(coeffs)):
                    power = len(coeffs) - i - 1
                    polynominal_value += coeffs[i] * np.power(x_float, power)

                return_value.append(polynominal_value)

            return return_value

def poly_prime(x):
    return_value = []
    for x_value in x:
        x_float = float(x_value)
        coeffs = []
        with open('poly.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                # print(str(row[0]))
                coeffs.append(float(row[0]))

            derevative_value = 0

            for i in range(len(coeffs)):
                power = len(coeffs) - i - 1
                derevative_value += power * coeffs[i] * np.power(x_float, power-1)

            return_value.append(derevative_value)

        return derevative_value
