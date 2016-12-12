# 모듈
# C 에선 #include <stdio.h>
# python 에선 improt 파일이름
# 참고! 변수는 못불러옴

import Header       # 이건 그 파일을 자체로 가져오는것 이고
from Header import b        # 이건 Header 에 있는 b라는 함수를 가져옴

print(Header.a())           # Header 에 a 함수
print(b())                  # Header 에 b 라는 함수

# 둘다 호출

# P.s 한번씩 해보면서 이해하는것이 좋음...
