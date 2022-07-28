# Tuple 튜블
# 리스트와 비교 중요
# 튜플 자료형( 순서ㅇ, 중복ㅇ, 수정X, 삭제X ) 불변(상수)
# 튜플 인덱스가 1개면 그데이터 타입을 따라간다.


# 튜플 선언
a = ()                                  # 타입 Tuple
b = (1)                                 # 타입 int
c = (11,12,13,14)
d = (100,1000,'Ace','Base', 'Captine')
e = (100,1000,('Ace','Base', 'Captine'))

print(type(a), type(b))                 # 결과 값 : <class 'tuple'> <class 'tuple'>

# 인덱싱 
print('>>>>>>>>>>>')
print('d - ', d[1])                     # 결과 값 : 1000
print('d - ', d[0]+d[1]+d[1])           # 결과 값 : 2100
print('d - ', d[-1])                    # 결과 값 : Captine
print('d - ', e[-1])                    # 결과 값 : ('Ace', 'Base', 'Captine')
print('d - ', e[-1][1])                 # 결과 값 : Base
print('d - ', list(e[-1][1]))           # 결과 값 : ['B', 'a', 's', 'e']   Tuple > list 형변환

# 수정 X 에러
# d[0] = 1500



# 슬라이싱
print('>>>>>>>>>>>')
print('d - ', d[0:3])                   # 결과 값 : (100, 1000, 'Ace')
print('d - ', d[2:])                    # 결과 값 : ('Ace', 'Base', 'Captine')
print('d - ', e[2][1:3])                # 결과 값 : ('Base', 'Captine')

# 튜플 연산
print('>>>>>>>>>>>')
print('c + d', c + d)                   # 결과 값 : (11, 12, 13, 14, 100, 1000, 'Ace', 'Base', 'Captine')
print('c * 3', c * 3)                   # 결과 값 : (11, 12, 13, 14, 11, 12, 13, 14, 11, 12, 13, 14)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ',a)                         # 결과 값 : (5, 2, 3, 1, 4)
print('a - ',a.index(3))                # 결과 값 : 2
print('a - ',a.count(2))                # 결과 값 : 1

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)                                # 결과 값 : ('foo', 'bar', 'baz', 'qux')
print(t[0])                             # 결과 값 : foo
print(t[-1])                            # 결과 값 : qux

# 언팩킹
(x1, x2,x3,x4) = t                       
print(type(x1),type(x2),type(x3),type(x4))# 결과 값 : <class 'str'> <class 'str'> <class 'str'> <class 'str'>
print(x1, x2,x3,x4)                     # 결과 값 : foo bar baz qux


# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6


print(t2)                                # 결과 값 : (1, 2, 3)
print(t3)                                # 결과 값 : (4,)
print(x1, x2, x3)                        # 결과 값 : 1 2 3
print(x4, x5, x6)                        # 결과 값 : 4 5 6