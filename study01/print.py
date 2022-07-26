#java System.out.println();과 같음
# Chapter02-1 
# Print 사용법

# 기본 출력
print("Hello World")                     # 결과값 : Hello World
print("Hello Python")                    # 결과값 : Hello Python
print('Python Start')                    # 결과값 : Python Start
print("Python Start")                    # 결과값 : Python Start
print('''Python Start''')                # 결과값 : Python Start
print("""Python Start""")                # 결과값 : Python Start

print()


# separator 옵션
print('P','Y','T','H','O','N', sep=' ')  # 결과값 : P Y T H O N
print('010','1234','5678', sep='-')      # 결과값 : 010-1234-5678
print('python','google.com', sep='@')    # 결과값 : python@google.com

print()

# end 옵션  
# end 옵션으로 print문 사이에 패턴추가가 가능하고 줄바꿈없이 문자를 길게 출력할 수 있음.

print('Welcome to', end=' ')
print('IT Mews', end=' ')
print('Web Site')                        # 결과값 : Welcome to IT Mews Web Site

print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용 (d, s, f) 
# 정수 d : 3 
# 문자열 s : 'Python' 
# 실수 f : 3.14
print('%s %s' % ('one', 'two'))           # 결과값 : one two
print('{} {}'.format('one', 'two'))       # 결과값 : one two
print('{1} {0}'.format('one', 'two'))     # 결과값 : two one

print()

# %s 문자열

print('%10s' %('nice'))                   # 결과값 :        nice (10자리를 확보하고 왼쪽부터 공백으로 채워짐)
print('{:>10}'.format ('nice'))

print('%-10s' %('nice'))                  # 결과값 :  nice       (10자리를 확보하고 오른쪽부터 공백으로 채워짐)
print('{:10}'.format ('nice'))

print('{:_>10}'.format ('nice'))          # 결과값 :  ______nice (10자리를 확보하고 왼쪽부터 -으로 채워짐)
print('{:^10}'.format ('nice'))           # 결과값 :     nice    (10자리를 확보하고 중앙정렬)

print('%.5s' % ('nice'))
print('%.5s' % ('PythonStudy'))           # 결과값 : Pytho
print('%5s' % ('PythonStudy'))            # 결과값 : PythonStudy
print('{:10.5}'.format('PythonStudy'))    # 결과값 : Pytho

# %d 정수   
print('%d, %d' % (1,2))                   # 결과값 : 1, 2
print('{},{}'.format (1,2))               # 결과값 : 1,2

print('%4d' % (42))                       # 결과값 :   42
print('{:4d}'.format(42))                 # 결과값 :   42

print()

# %f 실수
print('%f' % (3.143245234523))            # 결과값 :  3.143245
print('{:f}'.format(3.143245234523))      # 결과값 :  3.143245
print('%1.18f' % (3.143245234523))        # 결과값 :  3.143245234522999976 의미없는 부동소수점이 18개까지 출력

print('%06.2f' % (3.143245234523))        # 결과값 :  003.14
print('{:06.2f}'.format(3.143245234523))  # 결과값 :  003.14
