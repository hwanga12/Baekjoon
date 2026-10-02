# 아이디어: col 번째 값 기준 오름차순, 같으면 1번째 기준 내림차순 S_i -> i 번째 행 튜플에 대해 각 컬럼을 i로 나눈 나머지의 합. row_begin <= i <= row_end 인 모든 s_i 누적하여 하나의 값으로 환산.
# 시간복잡도: 2500x 500 -> save
# 자료구조: for문 사용

def solution(data, col, row_begin, row_end):    
    answer = 0
    data.sort(key=lambda row: (row[col - 1], -row[0]))
    
    for i in range(len(data)):
        current = 0
        if row_begin <= i+1 <= row_end:
            for j in range(len(data[i])):
                current += data[i][j] % (i+1)
            answer ^= current
    
    
    return answer