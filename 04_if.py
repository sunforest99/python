# if 문 문법 if 조건 :
# 파이썬은 중괄호를 안쓰므로 띄어쓰기에 따라 if문안에있나 밖에있나 구별
# 비교연산자
# a == b        a 와 b가 같을때
# a > b         a 가 b 보다 클때
# a < b         a 가 b 보다 작을때
# a >= b        a 가 b 보다 크거나 같을때
# a <= b        a 가 b 보다 작거나 같을때
# a != b        a 가 b 가 아닐때

if True:        # true 일때
    print("code1")      # code1 출력 (if 문 안)
    print("code2")      # code2 출력 (if 문 안)
print("code3")          #  code3 출력 (if 문 밖)

input = 11
real = 11
if real == input:       # real 와 input 이 같으면 출력
    print("Hello!")

# else 문
# else 문은 위에 if 문이 없으면 사용 불가
# 위의 if 문이 참이 아닐때 else 문으로 들어옴
input = 11
real = 11
if real == input:       # real 와 input 이 같으면
    print("Hello!")
else:                   # 위의 조건식이 아닐때
    print("Who are you?")

# elif(else if) 문
# elif 문은 위에 if 문이 없으면 사용 불가
# if -> elif -> else 사용가능
input = 33
real_egoing = 11
real_k8805 = "ab"
if real_egoing == input:        # real_egoing 이 input 일때
  print("Hello!, egoing")       # false 이므로 elif 로 검사
elif real_k8805 == input:       # real_egoing 이 input 일때
  print("Hello!, k8805")        # fale 이므로 else 문으로 검사
else:                           # 위에 둘다 아닐때
  print("Who are you?")         # true 이므로 출력
