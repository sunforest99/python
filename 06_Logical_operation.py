# 논리 연산자
# C 에서는 &&(and) ,||(or) ,! (not), ^(xor)
# python 에선 and(and), or(or), not a(not (a가 아니면 참))

# and
input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
real_id = "egoing"
real_pwd = "11"
if real_id == input_id and real_pwd == input_pwd:       # 둘다 참이여야 참
    print("Hello!")
else:
    print("로그인에 실패했습니다")

# or
in_str = input("아이디를 입력해주세요.\n")
real_egoing = "egoing"
real_k8805 = "k8805"
if real_egoing == in_str or real_k8805 == in_str:       # 둘중에 하나여야 참
  print("Hello!")
else:
  print("Who are you?")
