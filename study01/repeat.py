# 반복문 for while
# 파이썬 반복문

# for in <collection>
#   <Loop body>


from cmath import e
from xmlrpc.client import boolean


for v1 in range(10):                # 0~9
    print('vi is : ', v1)

print()

for v2 in range(1,11):              # 1~10
    print('v2 is : ', v2)

print()

for v3 in range(1,11,2):            # 1,3,5,7,9
    print('vi is : ', v3)


print()
# 1~1000 합
sum1 = 0
for v4 in range(1,1001):
    sum1 += v4

print('1~1000 sum : ', sum1)

print('1~1000 sum : ', sum(range(1, 1001)))
print('1~1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))



# Iterrables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterrables 리턴 함수 :  range, reversed, enumerate, filter, map, zip

# 예제 1 
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'You' ]
for n in names:
    print('names : ', n)

# 예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers : 
    print('lotto_numbers : ', n)

word = "Beautiful"

# 예제 3
for n in word:
    print('word : ', n)

# 예제 4
my_info = {
    'name' : 'Lee',
    'Age'  : 33,
    'City' : 'Inchone'
}

for key in my_info : 
    print('my_info : ', my_info[key])

for v in my_info.values() : 
    print('values : ', v)

# 예제 5

name = 'FineAppLE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())



# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for n in numbers : 
    if n == 34:
        print('break')
        break 
    else :
        print(n)

# continue
lt = ["1", 2, 5 ,True , 4.3, complex(4)]

for v in lt : 
    if type(v) is bool:
        continue
    print("type : " , v, type(v))
 
# for - else

numbers = [14, 3, 4, 7, 10, 21, 17, 2, 33, 15, 34, 36, 38]

for num in numbers : 
    if num == 24 :
        print('Found : 24')
        break
else:
    print('Not Found :  24')


# 구구단 출력

for i in range(2,10) :
    for j in range(1,10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))          # Id 값
print('List', list(reversed(name2)))        # List 형변환
print('tuple', tuple(reversed(name2)))      # Tuple 형변환
print('set', set(reversed(name2)))          # 순서 x

# while 실습
# while <expr> : 
#       <statement(s)>

# 예제 1
  
n = 6
while n > 0:
    n = n - 1
    print(n)