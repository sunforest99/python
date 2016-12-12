# 띄어쓰기를 주위합시다!!
def a3():       # a3 이라는 함수를 만들고
    print('aaa')        # aaa를 출력 (함수 안)
a3()                    # a3 이라는 함수 호출(함수 밖이겠지 :) )

def t3():       # t3 이라는 함수를 만들고
    return 'ttt'        # ttt를 반환 (함수 안)
print(t3())             # t3 이라는 함수 호출(출력) (함수 밖이겠지 :) )

def a(num):     # a 라는 인자값 받는 함수
    return 'a'*num      # a * 인자값 대로 반환 (함수 안)
print(a(3))             # a 라는 함수에 인자값 3 을 넣고 호출 (함수 밖)

def make_string(str, num):      # make_string 라는 함수에 문자열 , 숫자를 인자값으로 받고
    return str*num              # 문자열 * 숫자 (함수 안) 이거 이해안되면 01_pirnt.py 부터 봅세 (함수 안)
print(make_string('b', 3))      # make_string라는 함수에 문자열 b 를 넣고 3을 넣음 (함수 밖)

# 예제
# 위에 잘보고 전에 했던 if 문 과 for 문 을 알면 알아볼수 있음 :)
input_id = input("아이디를 입력해주세요.\n")
def login(_id):
    members = ['egoing', 'k8805', 'leezche']
    for member in members:
        if member == _id:
            return True
    return False
if login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')
