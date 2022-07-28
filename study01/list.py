# 리스트 List
# 리스트 자료형 (순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ)


# 선언
a = []
b = list()
c = [70, 75, 80, 85 ] #len 4
d = [1000, 10000, 'Aec', "Base", "Captine"]
e = [1000, 10000, ['Aec', "Base", "Captine"]]
f = [21.42, 'foobar', 3 , 4 ,False , 3.14159]


# 인덱싱
print('>>>>>>>>>')
print('d - ', type(d),d)                    # 결과 값 : <class 'list'> [1000, 10000, 'Aec', 'Base', 'Captine']
print('d - ', d[1])                         # 결과 값 : 10000
print('d - ', d[0] + d[1] +d[1])            # 결과 값 : 21000
print('d - ', d[-1])                        # 결과 값 : Captine
print('e - ', e[-1][1])                     # 결과 값 : Base
print('e - ', list(e[-1][1]))               # 결과 값 : ['B', 'a', 's', 'e']


# 슬라이싱
print('>>>>>>>>')
print('d - ', d[0:3])                       # 결과 값 : [1000, 10000, 'Aec']
print('d - ', d[2:])                        # 결과 값 : ['Aec', 'Base', 'Captine']
print('e - ', e[-1][1:3])                   # 결과 값 : ['Base', 'Captine']

# 리스트 연산
print('>>>>>>>>')
print('c + d', c + d)                       # 결과 값 : [70, 75, 80, 85, 1000, 10000, 'Aec', 'Base', 'Captine']
print('c * 3', c * 3)                       # 결과 값 : [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
print("'Test' + 'c[0]",'Test'+str(c[0]))    # 결과 값 : Test70



# 값 비교
print(c == c[:3] + c[3:])                   # 결과 값 : True
print(c)                                    # 결과 값 : [70, 75, 80, 85]
print(c[:3] + c[3:])                        # 결과 값 : [70, 75, 80, 85]
print()

# Identity(id)
temp = c
print(temp,c)
print(id(temp))             # 결과 값 : 4305795072 같은 데이터는 같은 주소로 복사 됨
print(id(c))                # 결과 값 : 4305795072 

# 리스트 수정, 삭제
print('>>>>>>>>')
c[0] = 4
print('c -', c)             # 결과 값 : [4, 75, 80, 85]
c[1:2] = ['a','b','c']      
print('c -', c)             # 결과 값 : [4, 'a', 'b', 'c', 80, 85] 슬라이싱 형태로 넣으면 이와같이 데이터가 들어감
c[1:2] = [['a','b','c']]
print('c -', c)             # 결과 값 : [4, ['a', 'b', 'c'], 'b', 'c', 80, 85] 대가로를 감싸주면 리스트안에 리스트형태로 들어감
c[1] =  ['a','b','c']
print('c -', c)             # 결과 값 : [4, ['a', 'b', 'c'], 'b', 'c', 80, 85] 슬라이싱없이 인덱스로 데이터를 주입하면 리스트안 리스트 형태로 들어감.
c[1:3] = []
print('c -', c)             # 결과 값 : [4, 'c', 80, 85] 인덱스 1부터 3번쨰까지 삭제
del c[2]
print('c -', c)             # 결과 값 : [4, 'c', 85] del 삭제 함수 (인덱스 2번쨰있는 데이터 삭제)


# 리스트 함수
a =  [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)                # 끝부분에 데이터를 추가하는 함수
print('a - ', a)
a.sort()                    # 정령관련 함수
print('a - ', a)
a.reverse()                 # 정령관련 함수 반대로
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)              # 데이터 삽입 관련 index 2번쨰 공간에 숫자 7을 추가
print('a - ', a)
# del a[6]
# print('a - ', a)
a.remove(10)                # 삭제관련 함수 해당 a 리스트에서 숫자 10을 전부 지운다.
print('a - ', a)
print('a - ', a.pop())      # pop함수 : index마지막 데이터를 추출 한다.(리스트에서 삭제)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))   # count함수 : 원하는 데이터를 입력하고 중복된 되이터의 갯수를 반환함 


ex = [8, 9]
a.extend(ex)                # entend함수 : 데이터 마지막에 데이터 삽입
print('a - ', a)


# 삭제 : remove, pop, del


# 반복문 활용
while a:                    # pop함수를 활용해서 마지막 index부터 하나씩 출력하고 값 제거
    data = a.pop()
    print(data)