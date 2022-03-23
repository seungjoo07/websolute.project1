
'''4.9'''

def display(S):
    for i in range(len(S)-1, -1, -1):
        print(S[i])

S = [1, 2, 3, 4, 5, 7]
display(S)

'''4.9'''


'''4.12'''

def isEmpty(s):
    return len(s) == 0
s = []
n = 4096
while n > 0:
    s.append(n % 2)
    n = n // 2
while not isEmpty(s):
    print(s)

'''4.12'''


'''4.13'''

values = []
for i in range(10):
    if i % 3 == 0:
        values.append(i)

print(values)


values = []
for i in range(20):
    if i % 3 == 0:
        values.append(i)
    elif i % 4 == 0:
        values.append(i)
print(values)

'''4.13'''
