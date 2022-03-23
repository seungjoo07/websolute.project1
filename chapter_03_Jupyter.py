

'''3.2'''
#insert를 하면 인덱스 위치에 삽입을 하고 다른 값들은 그 위치에서 한칸씩 밀려난다.'''
L = []
L.insert(0, 10)
L.insert(1, 20)
L.insert(0, 30)
L.insert(2, 40)
L.insert(len(L), 50)
print(L)

'''3.2'''


'''3.3'''
#insert를 하면 인덱스 위치에 삽입을 하고 다른 값들은 그 위치에서 한칸씩 밀려난다.'''

#-----------------------------------
#앞의 연산을 위한 3.2 코드
L = []
L.insert(0, 10)
L.insert(1, 20)
L.insert(0, 30)
L.insert(2, 40)
L.insert(len(L), 50)
print(L)
#앞의 연산을 위한 3.2 코드
#-----------------------------------

L.insert(1, 60)
print(L)
L[2] = 70
print(L)
L.pop(2)
print(L)

'''3.3'''




'''3.5'''

#-----------------------------------
#간단한 코드 내장함수 사용 방법'''
L = [1,4,2,6,7]
print(max(L))
#-----------------------------------

#-----------------------------------
#내장함수 미사용 방법
L = [1,4,2,6,7]

#maxValue 초기화 값에 L 리스트의 처음값 삽입 처음값부터 순차적으로 비교하기 위해서
maxValue = L[0]

for i in range(1, len(L)):
    if maxValue < L[i]:
        maxValue = L[i]

print(maxValue)
#-----------------------------------

'''3.5'''


'''3.7'''

# L1 리스트의 값들을 for문을 통해 순차적으로 반복하고
# if i in L2 문을 통해 값 i가 L2 리스트에 존재하는지 확인
def sameValueCheck(L1, L2):
    for i in L1:
        if i in L2:
            return True

    return False

# 같은 값이 존재하는 예제
L1 = [1, 2, 3, 4]
L2 = [5, 2, 6, 7]
sameValueCheck(L1, L2)
# 같은 값이 존재하는 예제

# 같은 값이 없는 예제
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
sameValueCheck(L1, L2)
# 같은 값이 없는 예제
'''3.7'''


'''3.8'''

#오름차순 정렬된 L1, L2 리스트를 받아
#extend()로 합치고 다시 정렬 후 반환
def mergeSort(L1, L2):

    L1.extend(L2)
    L1.sort()
    print(L1)

L1 = [6, 5, 8]
L2 = [1, 7, 5, 4, 5]
L1.sort()
L2.sort()
mergeSort(L1, L2)

'''3.8'''