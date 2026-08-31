def solution(clothes):
    answer = 0
    answer_ = 1
    clothes_dict = {}

    for i in range(len(clothes)):
        category = clothes[i][1]

        if category not in clothes_dict:
            clothes_dict[category] = 1
        else:
            clothes_dict[category] += 1

    for count in clothes_dict.values():
        answer_ *= count + 1

    answer = answer_ - 1

    return answer