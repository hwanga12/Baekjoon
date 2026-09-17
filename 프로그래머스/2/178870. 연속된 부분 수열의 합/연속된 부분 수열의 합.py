def solution(sequence, k):
    answer = []
    start_index = 0
    current_result = 0

    for end_index in range(len(sequence)):
        
        current_result += sequence[end_index]

        while current_result > k:
            current_result -= sequence[start_index]
            start_index += 1

        if current_result == k:
            if not answer or end_index - start_index < answer[1] - answer[0]:
                answer = [start_index, end_index]

    return answer