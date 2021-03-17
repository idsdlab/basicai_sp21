# calculator v1
import sys

if __name__ == '__main__':
    while True:
        x, y, op = input().split(',')
        # print(x, y, op)
        x = int(x)
        y = int(y)
        
        if op == '+':
            z = x + y
        elif op == '-':
            z = x - y
        elif op == '*':
            z = x * y
        elif op == '/':
            z = x / y
        else:
            print('need correct operator')
            sys.exit(0)
        
        print('value is : ', z)