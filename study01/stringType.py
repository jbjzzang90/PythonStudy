# 파이썬 문자형


# 문자열 생성
str1  = "I am Python"
str2  = 'Python'
str3  = """How are you?"""
str4  = '''Thank you!'''


print(type(str1),type(str2),type(str3),type(str4))    # 데이터타입 함수
print(len(str1),len(str2),len(str3),len(str4))        # 데이터크기, 길이

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))


# 이스케이프 문자 사용
"""
Escape 코드

\n   : 개행
\t   : 탭
\\   : 문자
\'   : 문자
\"   : 문자
\000 : 널 문자
"""
# I 'm Boy

print("I'm Boy")                # 결과 값 : I'm Boy
print('I\'m Boy')               # 결과 값 : I'm Boy

print('a \t b')                 # 결과 값 : a        b
print('a \n b')                 # 결과 값 : a  줄바 꿈 b
print('a \"\" b')               # 결과 값 : a "" b

print()


escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)              # 결과 값 : Do you have a "retro games"?
escape_str2 = 'What\'s on TV?'
print(escape_str2)              # 결과 값 : What's on TV?


# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)                     # 결과 값 : Click    Start!
print(t_s2)                     # 결과 값 : New Line 줄 바꿈  Check!
print()

# Raw String 앞에r 추가하면 이스케이프 문자가 적용되지 않는다.
raw_s1 = r'D:\python\test'
print(raw_s1)                   # 결과 값 : D:\python\test
print()


# 멀티라인 입력
# 역슬래시 사용
multi_str = \
'''
String
Multi line
test
'''
print(multi_str)

# 문자열 연산
str_01 = "Python"
str_02 = "Apple"
str_03 = "How are you doing"
str_04 = "Seoul Deajeon Busan JinJu"

print(str_01 * 3)               # 결과 값 : PythonPythonPython
print(str_01 + str_02)          # 결과 값 : PythonApple
print('y' in str_01)            # 결과 값 : True (문자에 y가 포함되있으면 True)
print('n' in str_01)            # 결과 값 : True (문자에 n가 포함되있으면 True)
print('P' not in str_02)        # 결과 값 : True (문자에 P가 포함되있으면 False)


# 문자열 형 변환
print(str(66),type(str(66)))    # 결과 값 : 66 <class 'str'>
print(str(10.1))                # 결과 값 : 10.1
print(str(True),type(str(True)))# 결과 값 : True <class 'str'> (문자 True로 인식)


# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha.....)

print("Capitalluze", str_01.capitalize())        # 첫번쨰 문자을 대문자로 변경하는 함수
print("endswith? : ", str_02.endswith("e"))      # 마지막 문자의 값이 무었인지 True & Flase로 반환
print("replace", str_01.replace("thon", 'Good')) # 해당 결과값에 thon이 포함되있으면 Good으로 변경하는 함수
print("sorted: ", sorted(str_01))