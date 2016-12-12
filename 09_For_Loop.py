# for 문
members = ['egoing', 'leezche', 'graphittie']
for member in members:
    print(member)

# item 이라는 변수를 선언후
# range(5,11) 을 대입 (5,11)인데 0부터 시작하므로 5 ~ 10 출력
for item in range(5, 11):
    print(item)

input_id = input("아이디를 입력해주세요.\n")      # 사용자에게 입력을 받고
members = ['egoing', 'k8805', 'leezche']        # 아이디 List 로 담고
for member in members:                          # 입력받은 아이디를 체크
    if member == input_id:                      # 일치하면 들어옴
        print('Hello!, '+member)
        import sys
        sys.exit()
print('Who are you?')                           # 아니면 출력
