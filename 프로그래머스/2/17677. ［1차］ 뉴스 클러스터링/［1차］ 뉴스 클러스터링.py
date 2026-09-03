def solution(str1, str2):
    answer = 0
    str1_ = []
    str2_ = []
    a = 0

    str1 = str1.lower()
    str2 = str2.lower()

    # 두 글자씩 잘라서 영문자로만 이루어진 경우만 저장
    for i in range(len(str1) - 1):
        pair = str1[i:i + 2]

        if pair.isalpha():
            str1_.append(pair)

    for i in range(len(str2) - 1):
        pair = str2[i:i + 2]

        if pair.isalpha():
            str2_.append(pair)

    # 다중집합의 교집합 개수 계산
    temp = str2_.copy()

    for i in range(len(str1_)):
        if str1_[i] in temp:
            a += 1
            temp.remove(str1_[i])

    # 합집합 개수
    union = len(str1_) + len(str2_) - a

    # 두 집합이 모두 공집합인 경우
    if union == 0:
        answer = 65536
    else:
        # 자카드 유사도에 65536을 곱하고 소수점 버리기
        answer = a * 65536 // union

    return answer