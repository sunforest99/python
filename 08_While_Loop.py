# While
while False:
    print('Hello world')
print('After while')

# 반복조건
i = 0
while i < 3:
    print('Hello world')
    i = i + 1

# 반복조건의 활용
i = 0
while i < 10:
    print('print("Hello world '+str(i*9)+'")')
    i = i + 1

# 조건문과 반복문의 합체
i = 0
while i < 10:
    if i == 4:
        print(i)
    i = i + 1

# 요것도
i = 0
while i < 10:
    if i == 4:
        break
    print(i)
    i = i + 1
print('after while')
# 반복문의 조건은 알꺼라 믿고 생략
# break 는 함수나 반복문 안에 쓸시에 함수나 반복문을 탈출한다
# *중요 증감식은 꼭 써줘야된다(안그러면 무한루프를 돈다) 무한루프를 돌리려면 while 문 조건에 true 나 1을 써주면 된다.

# List 와 whle 문
members = ['egoing', 'leezche', 'graphittie']
i = 0
while i < len(members):         # List 의 원소 개수
    print(members[i])
    i = i + 1
