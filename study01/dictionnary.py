# 파이썬 딕셔너리 json 형태랑 비슷
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서x, 키 중복x, 수정ㅇ, 삭제ㅇ)
# ()튜플 []리스트 {}딕셔너리

# 선언
a = {'name':'jeong','phone': '01011112222', 'birth' :'900709'}
b = {0:'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name' : 'Byeongnam',
    'City' : 'Incheon',
    'Age' : '33',
    'Grade' : 'A',
    'Status': True
}
e = dict([
    ('Name', 'Byeongnam'),
    ('City', 'Incheon'),
    ('Age', '33'),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Byeongnam',
    City = 'Incheon',
    Age = 33,
    Grade = 'A',
    Status = True
)

# 출력 
print('a =', type(a),a)
print('b =', type(b),b)
print('c =', type(c),c)
print('d =', type(d),d)
print('e =', type(e),e)
print('f =', type(f),f)


print()
print('a - ', a['name'])            # 키가 존재하지 않으면 -> 에러발생
print('a - ', a.get('name'))        # 키가 존재하지 않으면 -> None로 처리 됨
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Incheon'
print(a)
a['rank']=[1, 2, 3]
print(a)


print('a = ', len(a))
print('b = ', len(b))
print('c = ', len(c))
print('d = ', len(d))
print('e = ', len(e))


print('a = ', a.keys())                 # key값만 가져오는 함수
print('b = ', b.keys())
print('c = ', c.keys())
print('d = ', d.keys())

print('a = ', list(a.keys()))
print('b = ', list(b.keys()))
print()

print('au = ', a.values())              # value값만 가져오는 함수
print('b = ', b.values())
print('c = ', c.values())
print('d = ', d.values())

print('a = ', list(a.values()))
print('b = ', list(b.values()))


print('a = ', a.items())                #  key, value 가져오는 함수(dict_items)
print('b = ', b.items())
print('c = ', c.items())


print('a = ', list(a.items()))
print('b = ', list(b.items()))
print()

print('a = ', a.pop('name'))
print('a = ', a)
print('c = ', c.pop('arr'))
print('c = ', c)
print()

print('f - ', f.popitem())
print('f - ', f)
print()

print('a = ', 'birth' in a)
print('a = ', 'Cirth' in b)


# 수정 # 추가
a['test'] = 'test_dict'             # test key 추가
print('a = ',a)                     # 결과 값 : {'phone': '01011112222', 'birth': '900709', 'address': 'Incheon', 'rank': [1, 2, 3], 'test': 'test_dict'}

a['address'] = 'dj'                 # address 값 변경
print('a = ',a)                     # 결과 값 : {'phone': '01011112222', 'birth': '900709', 'address': 'dj', 'rank': [1, 2, 3], 'test': 'test_dict'}

a.update(birth = '900904')          # update 함수
print('a = ',a)                     # 결과 값 : {'phone': '01011112222', 'birth': '900904', 'address': 'dj', 'rank': [1, 2, 3], 'test': 'test_dict'}



