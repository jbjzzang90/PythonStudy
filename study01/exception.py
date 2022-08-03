# 파이썬 예외처리
# Exception
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError.....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 반긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True 

# NameError : 참조가 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100/0)

# IndexError : 없는 인덱스 값을 출력 시
# x = [50, 60, 70]
# print(x[1])
# print(x[4])  IndexError


# KeyError : 없는 딕셔너리 키값을 사용지 error
# dic = {'name' : 'Lee','Age':41,'City' : 'Busan'}
# print(dic['qqq']) Error
# print(dic.get('qqq')) None

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError : 자료구조 안에서 존재하지 않으면 발생
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError : 현제 경로에 파일이 없을때.
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'
# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y)) 이런식으로 형변환을 해야 에러발생을 안함


# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# excipt 에러명1: 여러개 가능
# excipt 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Pack']

# 예제 1
# try :
#     z = 'JeongZX'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except ValueError:
#     print('Not Found it! - Occurred ValueError!')
# else:
#     print('OK! else.')
# print()

# 예제 2
# try :
#     z = 'Jeong'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception:
#     print('Not Found it! - Occurred ValueError!')
# else:
#     print('OK! else.')
# print()

# 예제 3
# try :
#     z = 'Jeong'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x+1))
# except Exception as e:  # 에러 로그를 남길 수 있다.
#     print(e)
#     print('Not Found it! - Occurred ValueError!')
# else:
#     print('OK! else.')
# finally:
#     print('OK! finally!')
# print()


# 예제 4
# 예외 발생 : raise
# raise 키워드로 예뢰 집적 발생

try:
    a = 'Pack1'
    if a == 'Pack':
        print('OK! Pass!')
    else : 
        raise ValueError
except ValueError : 
    print('Occurred! Exception!')
else:
    print('OK! else!')