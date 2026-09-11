def solution(files):
    def make_key(file):
        # HEAD의 끝, NUMBER의 시작 위치 찾기
        i = 0

        while i < len(file) and not file[i].isdigit():
            i += 1

        head = file[:i]

        # NUMBER의 끝 위치 찾기
        j = i

        while (
            j < len(file)
            and file[j].isdigit()
            and j - i < 5
        ):
            j += 1

        number = file[i:j]

        return head.lower(), int(number)

    files.sort(key=make_key)

    return files