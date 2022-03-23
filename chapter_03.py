
"""3.2~3.3"""
def list_3_2_3(L):
    L.insert(0, 10)
    L.insert(1, 20)
    L.insert(0, 30)
    L.insert(2, 40)
    L.insert(len(L), 50)
    print(L)

    L.insert(1, 60)
    print(L)
    L[2] = 70
    print(L)
    L.pop(2)
    print(L)


"""3.7"""
def sameValueCheck(L1, L2):

    small = []
    big = []

    if (len(L1) >= len(L2)):
        big = L1
        small = L2
    else:
        big = L2
        small = L1

    for i in big:
        if i in small:
            return True

    return False


"""3.8"""
def mergeSort(L1, L2):

    L1.extend(L2)
    L1.sort()
    print(L1)



"""P3.3"""
def contains(set_em, val):
    i = -1
    for v in set_em:
        i += 1
        if val == v:
            return i

    return -1

def delete(set_em, val):
    list_em = list(set_em)
    index = contains(list_em, val)
    if index > -1:
        list_em.pop(index)

    return set(list_em)

def union(listA, listB):

    for i in listA:
        index = contains(listB, i)
        if index > -1:
            listB.pop(index)

    listA.extend(listB)

    setC = set(listA)

    return setC

def intersect(listA, listB):

    listC = []
    for i in listA:
        index = contains(listB, i)
        if index > -1:
            listC.append(listB.pop(index))

    setC = set(listC)

    return setC

def difference(listA, listB):

    removeList = []
    for i in listA:
        index = contains(listB, i)
        if index > -1:
            removeList.append(i)

    for i in removeList:
        listA.remove(i)
        listB.remove(i)
    listA.extend(listB)
    setC = set(listA)

    return setC

if __name__ == '__main__':
    """3.8
    L1 = [6, 5, 8]
    L2 = [1, 7, 5, 4, 5]
    L1.sort()
    L2.sort()
    mergeSort(L1, L2)
    """

    """P3.3"""
    set_em = {2,3,4}

    if (contains(set_em,2) > -1):
        print(True)
    else:
        print(False)

    print(delete(set_em, 4))

    listA = [1, 2, 3, 5, 6, 7]
    listB = [1, 7, 3, 4]
    print(union(listA, listB))

    listA = [1, 7, 3, 4]
    listB = [1, 2, 3, 5, 6, 7]
    print(intersect(listA, listB))

    listA = [1, 7, 3, 4]
    listB = [1, 2, 3, 5, 6, 7]
    print(difference(listA, listB))


    '''3.5'''

    L = [1,2,8,6,7]

    print(max(L))