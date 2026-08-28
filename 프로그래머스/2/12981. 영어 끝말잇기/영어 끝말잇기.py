def solution(n, words):
    used = set()

    for i, word in enumerate(words):
        duplicate = word in used
        wrong_connection = i > 0 and words[i - 1][-1] != word[0]

        if duplicate or wrong_connection:
            return [i % n + 1, i // n + 1]

        used.add(word)

    return [0, 0]