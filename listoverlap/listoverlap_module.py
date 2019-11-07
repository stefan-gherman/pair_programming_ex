import random as rdd

def listoverlap(list1, list2):
    
    similar = 0
    intersect = []
    for elem in list1:
        if elem in list2:
            similar = 1
            if elem not in intersect:
                intersect.append(elem)
    if similar == 0:
        return None
    else:
        return intersect    


def main():
    list_len_1 = rdd.randint(1,20)
    list_len_2 = rdd.randint(1,20)

    list_1 = []
    list_2 = []

    while list_len_1 > 0:
        list_1.append(rdd.randint(1,100))
        list_len_1 -= 1

    while list_len_2 > 0:
        list_2.append(rdd.randint(1,100))
        list_len_2 -= 1   

    print(listoverlap(list_1, list_2))
    #print(list_1)
    #print(list_2)

    print("I've got the gift of one liners:", str(set(list_1)&set(list_2)))

    return


if __name__ == '__main__':
    main()
