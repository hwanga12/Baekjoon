def solution(record):
    answer = []
    name = {}

    # 최종 닉네임 저장 + 입퇴장 사건 저장
    for i in range(len(record)):
        parts = record[i].split()

        a = parts[0]
        b = parts[1]

        if a == "Enter":
            c = parts[2]
            name[b] = c
            answer.append((a, b))

        elif a == "Leave":
            answer.append((a, b))

        elif a == "Change":
            c = parts[2]
            name[b] = c

    result = []

    # UID를 최종 닉네임과 매칭
    for a, b in answer:
        if a == "Enter":
            result.append(name[b] + "님이 들어왔습니다.")

        elif a == "Leave":
            result.append(name[b] + "님이 나갔습니다.")

    return result