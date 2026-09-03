def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []

    def dfs(current):
        if len(current) == 5:
            return

        for vowel in vowels:
            next_word = current + vowel
            words.append(next_word)
            dfs(next_word)

    dfs("")

    return words.index(word) + 1