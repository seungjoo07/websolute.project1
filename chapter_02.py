
def calc_perimeter(radius):
    global perimeter
    print("파이 값:", pi)
    perimeter = 2*pi * radius


'''2.1'''
def gugudan_for(dan):

    for i in range(1, 10):
        print(str(dan) + " X " + str(i) + " = " + str(dan*i))

'''2.2'''
def gugudan_while(dan):
    i = 1
    while (i < 10):
        print(str(dan) + " X " + str(i) + " = " + str(dan*i))
        i += 1

'''2.3'''
def gugudan_for_revers(dan):

    for i in range(9, 0, -1):
        print(str(dan) + " X " + str(i) + " = " + str(dan*i))

'''2.4'''
def cToF(val):
    return (32 + (180/100) * val)


'''2.6'''
def reverseList(inputList):
    cnt = 0
    i = -1
    while (cnt < len(inputList)):
        print(inputList[i])
        cnt += 1
        i -= 1

'''2.8'''
def listSum(inputList):
    i = 0
    sum = 0
    while (i < len(inputList)):
        sum += inputList[i]
        print(sum)
        i += 1

'''2.9'''
def dictMenu(inputDic):

    for menu in inputDic:
        print(menu)


'''2.11'''
def recursion_2_11 (n):

    if n == 1:
        return 1
    else:
        result = n + recursion_2_11(n-1)
        print(result)
        return result

'''2.12'''
def recursion_2_12 (n):


    if n == 1:
        return 1
    else:
        result = 1/n + recursion_2_12(n-1)
        print(result)
        return result

'''2.17'''
def printNum (n):

    for i in range(1, n+1):
        print(i)

def printRevNum (n):

    for i in range(n, 0, -1):
        print(i)



'''P2.2'''
def updownGame ():
    answer = 67
    min = 0
    max = 99

    for i in range(10):
        print("숫자를 입력하세요 (범위: " + str(min) + "~" + str(max) + "): ", end=" ")
        guess = int(input())

        if (answer == guess):
            print("정답입니다. " + str(i+1) + "번 만에 맞추셨습니다.")
            print("게임이 끝났습니다.")
            break
        else:
            if (guess > answer):
                print("아닙니다. 더 작은 숫자입니다!")
                max = guess
            if (guess < answer):
                print("아닙니다. 더 큰 숫자입니다!")
                min = guess


'''P2.3'''
def pyramidGame (h):
    val = 1
    center = h-1
    outCnt = 0


    for i in range(h):
        outline = ""
        val = 1
        j = 0

        while (j < h*2):
            if (center - outCnt) <= j and j <= (center + outCnt):
                if (val >= 10 and val < 100):
                    outline += " " + str(val)
                else:
                    outline += " " + str(val) + " "
                if j >= h-1:
                    val -= 2
                elif j < h-1:
                    val += 2
            else:
                outline += "   "
            j += 1
        outCnt += 1
        print(outline)





if __name__ == '__main__':
    """
    menuDict = {"콩나물해장국":4500, "갈비탕":9000, "돈가스":8000}
    menuDict["팟타이"] = 7000
    dictMenu(menuDict)
    """
    updownGame()

    """
    print("피라미드의 높이를 입력하세요: ", end="")
    h = int(input())
    pyramidGame(h)
    """
    """
    pi = 3.14159
    perimeter = 0
    calc_perimeter(10)
    print("원둘레(r=10) = ", perimeter)
    """
    """
    tmp_list = [1, 2, 3]
    reverseList(tmp_list)
    """














