# lab-03

def lab03_function(list_a):

    sum = 0
    for element in list_a:
        sum += element
    
    average = sum / len(list_a)

    count = 0
    for element in list_a:
        if element < average:
            count += 1

    return count

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # print(len(list_a))
    count = lab03_function(list_a)
    print(count)

    list_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
    count = lab03_function(list_a)
    print(count)