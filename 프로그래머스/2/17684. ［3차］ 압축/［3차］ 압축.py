def solution(msg):
    answer = []
    dictionary = {}

    for i in range(26):
        alphabet = chr(ord('A') + i)
        dictionary[alphabet] = i + 1

    next_index = 27
    i = 0

    while i < len(msg):
        w = msg[i]
        j = i + 1

        
        while j < len(msg) and w + msg[j] in dictionary:
            w += msg[j]
            j += 1

        answer.append(dictionary[w])

        if j < len(msg):
            dictionary[w + msg[j]] = next_index
            next_index += 1

        
        i += len(w)

    return answer