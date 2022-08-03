# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
# __init__.py : python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천

# 예제1  (같은 프로젝트일 경우 sub1패키지안에 module1.py를 사용)
import sub1.module1
import sub2.module2

# 사용
sub1.module1.mod1_test1()
sub1.module1.mod1_test2()

sub2.module2.mod2_test1()
sub2.module2.mod2_test2()

print()
print()
print()


# 예제 2
from sub1 import module1
from sub2 import module2 as m2 #alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제 3
from sub1 import * # 전체 소스를 가져올 수 있지만(불필요한 소스까지 전부 import되어서 권장하지 않음.)
from sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

# 예제 4
import sub3.module3

sub3.module3.test01()