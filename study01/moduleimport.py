# 모듈 가용 실습

import imp
import sys
import time



# print(sys.path)
# print(time.time())
print(type(sys.path))

# 모듈 경로 삽입 (해당소스에만 파일경로 삽입, 모든소스에사 가져다 쓰려면 파이선 path에 등록해줘야함.)
# sys.path.append('/Users/jeongbyeongnam/PythonStudy/PythonStudy-1')
print(sys.path)

import module

# 모듈 사용
print(module.power(10,3))

