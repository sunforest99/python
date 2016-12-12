class col(object) :                 # (object)는 상속입니다 생략해도됨 :) 상속하고싶을때 (클래스이름)  하면 됩니다
    def __init__(self,v1,v2) :      # 생성자입니다 self는 꼭 넣어주세요 self 라는건 인스턴스라는거임 모르면 검색 ㄱ
        print(v1,v2)

c1 = col(10,20)

'''
오버라이드는 함수 재정의임 이해할꺼라 믿음 ><
오버라이드 란?
같은 함수이름, 같은 인자값 인 함수를 다시 정의하는거임 (단 상속되있어야됨)
예를들어

class C1:
    def m(self):
        return 'parent'
class C2(C1):
    def m(self):
        return super().m() + ' child'
    pass
o = C2()
print(o.m())

이런식으로
'''
