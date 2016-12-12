# 파이썬에선 주석을 앞에다 #을 붙힘
'''
여러줄 주석은 위아레 작은따옴표 3개
'''
print(10)       # 10 출력

print('Hello')      # Hello
print("Hello")      # Hello
print("Hello 'world'")      # Hello 'world' 작은 따음표 출력
print('Hello "world"')      # Hello "World"

print('Hello '+'world')     # Hello World
print('Hello '*3)           # Hello 3번 출력
print('Hello'[0])           # 문자열에 첫번째 배열
print('Hello'[1])           # 문자열에 두번째 배열
print('Hello'[2])           # 문자열에 세번째 배열

print('hello world'.capitalize())       # 첫번째가 소문자면 대문자로 해서 출력
print('hello world'.upper())            # 소문자 -> 대문자 출력
print('hello world'.__len__())          # 문자열 개수 출력
print(len('hello world'))                # 문자열 개수 출력
print('Hello world'.replace('world', 'programming'))    # Hello world 에서 world -> programming 으로 바꿔서 출력

# 특수문자
print("egoing's \"tutorial\"")
print("\\")                     # \ 한개 출력
print("Hello\nworld")
print("Hello\t\tworld")         # 텝
print("\a")                     # 빈칸
print('Hello\nworld')           #\n 개행

#문자와 숫자를 통해서 알아보는 데이터 타입
print(10+5)         # 15
print("10"+"5")     # 105
