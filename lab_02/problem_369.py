#problem 369
def game369(number=1):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
            current = current // 10
    
    return count

if __name__ == '__main__':
    print('369 게임')
    
    number = int(input('숫자를 입력하세요 : '))
    count = game369(number=number)
    print('박수친 숫자는 : %d' % count)