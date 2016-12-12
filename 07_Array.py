# Array C 에서 배열
# List python 에서 배열
# type() 이란 함수는 데이터형식을 알려줌
# 배열은 대괄호를 써서 그 안에다 내용을

print(type('egoing')) #<class 'str'>        # 데이터타입을 출력 'str'(문자열 데이터)
name = 'egoing'
print(name) #egoing
print(type(['egoing', 'leezche', 'graphittie'])) #<class 'list'>
names = ['egoing', 'leezche', 'graphittie']
print(names)            # 리스트를 프린트하면 리스트에 속해있는 데이터들을 버여줌
print(names[2]) #graphittie     # 리스트에 있는 각각 인덱스를 호출하려면 배열처럼 쓰면된다. (0에서부터)
egoing = ['programmer', 'seoul', 25, False]
egoing[1] = 'busan'     # 1번 인덱스에 있는 값을 busan 으로 바꿈ㄴ
print(egoing) #['programmer', 'busan', 25, False]

# List 심화
al = ['A', 'B', 'C', 'D']
print(len(al)) # 4      # List 안에 있는 원소 갯수
al.append('E')      # List 에 값 추가
print(al) #['A', 'B', 'C', 'D', 'E']
del(al[0])      # 0번 인덱스 삭제
print(al) #['B', 'C', 'D', 'E']

# 여기에 없는 함수들
'''
 Solt() 정렬함수
 Reverse() 뒤집기
 insert(index, value) 요소삽입 등등...
'''
