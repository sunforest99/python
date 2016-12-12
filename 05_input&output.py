# input (입력)
in_str = input("입력해주세요.\n")        # in_str 이라는 변수에 사용자가 입력하는 값을 넣음
print(in_str.upper()+" World!")         # 만약 hello 를 입력했다면 HELLO world 로 출력

# 간단한 로그인 기능 만들기
# if 문은 앞에서 설명했기 때문에 알거라 믿음
in_str = input("아이디를 입력해주세요.\n")
real_egoing = "11"
real_k8805 = "ab"
if real_egoing == in_str:
  print("Hello!, egoing")
elif real_k8805 == in_str:
  print("Hello!, k8805")
else:
  print("Who are you?")
