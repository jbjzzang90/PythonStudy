# Chapter02-2 
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)                    #출력값 : 700
print(type(n))              #출력값 : <class 'int'>
print()

# 동시 선언
x = y = z = 700
print(x,y,z)                #출력값 : 700 700 700
print()

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)                  #출력값 : Change Value
print(type(var))            #출력값 : <class 'str'>
print()


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력


# 예1)
print(300)
print(int(300))
print()

# 예2)
# n -> 777
n = 777

print(n,type(n))
print()

m = n
# m - >  777 < - n
print(n,m)
print(type(n),type(m))
print()

m = 400

print(n,m)
print(type(n),type(m))
print()

# id(identity)확인 : 객체의 고유 값 확인.
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()


# 같은 오브젝트를 참조!
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언  
# Camel Case : helloPython -> Method
# Pascal Case : HelloPython -> Class
# Snake Case : hello_python -> 변수에 사용

# 허용하는 변수 선언 법
age = 1
Age = 1
aGe = 1
AGE = 1
a_g_e = 1
_age = 1
age_ = 1
_AGE_ = 1
AGE = 1

# 예약어는 변수명으로 선언 불사능
"""
and	except	lambda	with
as	finally	nonlocal	while
assert	false	None	yield
break	for	not	
class	from	or	
continue	global	pass	
def	if	raise	
del	import	return	
elif	in	True	
else	is	try	
"""


