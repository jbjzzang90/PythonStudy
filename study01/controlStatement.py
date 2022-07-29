# 파이썬 제어문
# if 실습


# 기본 형식
print(type(True))       # 0이 아닌 수, "abc",
print(type(False))      # 0, "", [], (), {}...


# 예1
if True:
    print('Good')
if False:
    print('Bad')

# 예2
if True : 
    print('Good')
else:
    print('Bad')

# 관계 연산자
# >, >=, <, <=, ==, !=

x = 15
y = 10

# 양변이 같은 경우 참
print(x == y)

# 양변이 다를 때 참
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

# 예3
city = ""
if city : 
    print("You are in : ", city)
else :
    print("plz enter your city ")

# 예4
city2 = "Incheon"
if city2 : 
    print("You are in : ", city2)
else :
    print("plz enter your city ")


# 논리연산자
# and, or, not

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)
print('or : ', a > b or b > c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 >  관계 > 논리
print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

# 예4
# 복수의 조건이 모두 참일 경우에 실행
score1 = 80
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('pass')
else : 
    print('fail')


# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin' : 
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')


# 예6 다중조건문

num = 60

if num >= 90:
    print('Grede : A')
elif num >= 80:
    print('Grede : B')
elif num >= 70:
    print('Grede : C')    
else :
    print('과락')


# 예7 중첩조건문

grede = 'A'
total = 95

if grede == 'A':
    if total >= 90 : 
        print('장학음 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')    
else :
    print('장학금 없음')


# in, not in

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name" : "Jeong", "city" : "Incheon", "Grede": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Incheon" in e.values())