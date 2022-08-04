# 파일 읽기 및 쓰기
# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./'), 절대 경로('예 C:\Python\....')


# 파일 읽기(Read)
# 예제 1

# f = open('/Users\\jeongbyeongnam\\PythonStudy\\PythonStudy-1\\resource\\it_news.txt') # 절대 경로
f = open('./resource/it_news.txt','r', encoding='UTF-8')
# 속성 확인
print(dir(f))               
# 인코딩 확인
print(f.encoding)           # 결과 값 : UTF-8
# 파일 이름
print(f.name)               # 결과 값 : ./resource/it_news.txt
# 모드 확인
print(f.mode)               # 결과 값 : r
cts = f.read()
print(cts)
# 반드시 Close
f.close()


# 예제 2 (with문은 close를 안해줘도됨)

with open('./resource/it_news.txt','r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()


# 예제 3
# read() :  전체 읽기 , read(10) : 10Byte 크기만 읽어온다

with open('./resource/it_news.txt','r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)                # Right now gamers can
    c = f.read(20)
    print(c)                # pay just $1 for acc
    f.seek(0,0)             # 처음으로 초기화하는 함수
    c = f.read(20)
    print(c)

print()


# 예제 4
# readline : 한줄씩 읽어온다
with open('./resource/it_news.txt','r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()


# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt','r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts : 
        print(c, end='')
    
print()


# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love Python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love Python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
with open('./resource/contents2.txt', 'w') as f:
    print('Test text Write', file=f)
    print('Test text Write', file=f)
    print('Test text Write', file=f)
    

# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv
# 예제 1
import csv
import re
from turtle import right

from nbformat import read
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # Header Skip
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))  #__iter__
    print()
    
    for c in reader : 
        # print(c)
        # print(type(c)) list
        print(' '.join(c))


# 예제 2 
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')

    for c in reader:
        print(c)


# 예제 3 딕셔너리 형태
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('--------')

# 예제 4 리스트
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    # print(dir(wt))
    # type 확인
    # print(type(wt))
    
    for v in w :
        wt.writerow(v)
    
         

# 예제 5

with open('./resource/write2.csv', 'w', encoding='utf-8') as f:
        # 필드명
        fields = ['One', 'Two', 'Three']

        # Dict Writer
        wt =  csv.DictWriter(f, fieldnames=fields)

        wt.writeheader()

        for v in w:
            wt.writerow({'One':v[0],'Two':v[1],'Three':v[2]})

