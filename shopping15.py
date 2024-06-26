import hashlib

def get_md5_hash(input_string):
# MD5 해시 객체 생성
    md5_hash = hashlib.md5()

    # 입력 문자열을 바이트로 인코딩하여 해시 객체에 추가
    md5_hash.update(input_string.encode('utf-8'))

    # 해시 계산
    md5_digest = md5_hash.hexdigest()

    # 해시 값 출력
    #print("MD5 해시 값:", md5_digest)

    # 해시 값의 처음 두 글자 추출
    first_two_chars = md5_digest[:2]

    return first_two_chars

# 테스트할 입력 문자열
for i in range (0, 127):
    input_string = "Eqstmyeieoom" + chr(i)
    result = get_md5_hash(input_string)
    print(chr(i), "해시 값의 처음 두 글자:", result)

# MD5 해시 값 계산 및 처음 두 글자 추출
#EqstmyeiygoKb72