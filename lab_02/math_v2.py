# sin(x)
import math

def derivative_of_sin(x):
    return math.cos(x)

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_sin(x):
    return math.sin(x)
    
if __name__ == '__main__':
    while True:
        x = input('input x: ')
        x = float(x)
        y = numerical_diff(function_sin, x)
        z = derivative_of_sin(x)
        abs_diff = abs(y - z)
        print('x is ', x, 'derivative of sin(x): ', z, 'numerical diff: ', y, 'abs diff: ', abs_diff)