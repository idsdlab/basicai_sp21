# lab-04
# reference : https://blog.winterjung.dev/2020/01/06/floating-point-in-python
import decimal

def lab04_function(speed, list_a):

    # rule1 = float(speed * 1.1)
    # rule2 = float(speed * 1.2)
    # rule3 = float(speed * 1.3)

    rule1 = float(speed * decimal.Decimal('1.1'))
    rule2 = float(speed * decimal.Decimal('1.2'))
    rule3 = float(speed * decimal.Decimal('1.3'))
    
    violate1_cnt = 0
    violate2_cnt = 0
    violate3_cnt = 0

    for element in list_a:
        element_f = float(element)

        if element >= rule1 and element < rule2:
            violate1_cnt += 1

        if element >= rule2 and element < rule3:
            violate2_cnt += 1

        if element >= rule3:
            violate3_cnt += 1
        
    # print(violate1_cnt, violate2_cnt, violate3_cnt)
    return violate1_cnt * 3 + violate2_cnt * 5 + violate3_cnt * 7

if __name__ == '__main__':
    cars = [110, 98, 125, 148, 120, 112, 89]
    speed = 100

    # print(len(list_a))
    total_fine = lab04_function(speed, cars)
    print(total_fine)
