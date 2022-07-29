# 집합 (set) 특징
# 집합 (set) 자료형(순서X, 중복X)


# 선언 
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}   # key가 없으면 set() key가 있으면 딕셔너리
f = {42, 'foo', (1, 2, 3), 3.14159}

# 출력
print('a = ', type(a),a)
print('b = ', type(b),b)
print('c = ', type(c),c)
print('d = ', type(d),d)
print('e = ', type(e),e)
print('f = ', type(f),f)

# 튜플 변환 (set -> tuple)
t =  tuple(b)
print('t = ', type(t),t)                # 결과 값 : <class 'tuple'> (1, 2, 3, 4)
print('t = ', t[0],t[1:3])              # 결과 값 : 1 (2, 3)


# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)

print('1 =',l)                          # 결과 값 : [1, 4, 5, 6]
print('12 =',l2)                        # 결과 값 : ['foo', 'bar', 'qux', 'baz']


# 길이
print('a = ', len(a))
print('b = ', len(b))
print('c = ', len(c))
print('d = ', len(d))
print('e = ', len(e))

# 집합 자료형 활용
s1 =  set([1, 2, 3, 4, 5, 6])
s2 =  set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)                # 결과값 :  {4, 5, 6}
print('s1 & s2 : ', s1.intersection(s2))    # 결과값 :  {4, 5, 6} (교집합)

print('s1 | s2 : ',s1 | s2)                 # 결과값 :  {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2 : ',s1.union(s2))            # 결과값 :  {1, 2, 3, 4, 5, 6, 7, 8, 9} (합집합)

print('s1 - s2 : ', s1 - s2)                # 결과값 :  {1, 2, 3} (차집합)
print('s1 - s2 : ', s1.difference(s2))      # 결과값 :  {1, 2, 3}

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))      # 교집합이있으면 False

# 부분 집합 확인
print(s1.issubset(s2))
print(s1.issuperset(s2))


# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 = ', s1)                      # 결과 값 : {1, 2, 3, 4, 5}

s1.remove(2)                            # remove함수로 없는값을 지우면 에러가 발생한다
print('s1 = ', s1)                      # 결과 값 : {1, 3, 4, 5}

s1.discard(3)                           # remove와 같은 기능인데 없는값을 지워도 에러가 발생하지 않는다.
print('s1 = ', s1)                      # 결과 값 : {1, 4, 5}
s1.clear()                              # 전체삭제하는 함수 (list, set)에서 사용가능.
print('s1 = ', s1)                      # 결과 값 : set()