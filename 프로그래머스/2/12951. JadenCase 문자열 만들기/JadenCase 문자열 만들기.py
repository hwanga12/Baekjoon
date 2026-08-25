def solution(s):
    words = s.split(" ")
    answer = []

    for word in words:
        if word == "":
            answer.append("")
            continue

        if word[0].isdigit():
            answer.append(word[0] + word[1:].lower())
        else:
            answer.append(word[0].upper() + word[1:].lower())

    return " ".join(answer)