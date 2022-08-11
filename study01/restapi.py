import gitlab
import requests
import json
# pip3 install python-gitlab (터미널에서 python-gitlab 다운로드)
# 참조 https://python-gitlab.readthedocs.io/en/stable/api-usage.html

# gitlab.Gitlab('프로젝트url'  private_token=[토큰id]
account = gitlab.Gitlab('URL', private_token='토큰ID') 
account.auth() # 계정인증
projects= account.projects.list(Iterator=True)  # 프로젝트 전체리스트
print(type(projects))
for project in projects :
    print(project)





# requests 사용하여서 추출
response = requests.get('URL', headers={"PRIVATE-TOKEN":"토큰ID"})
print(response.text)
print(type(response.text))          # 문자열

print("------"*10)

json_data = json.loads(response.text)
print(type(json_data))              # 리스트

for listtest in json_data:
    print("asdasdasdasd " ,listtest)
    print("asdasdasdasd " ,listtest.get('id'))
