def solution(numbers):
    answer = []

    for number in numbers:
    
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bits = "0" + bin(number)[2:]

            zero_index = bits.rfind("0")

            bits = (
                bits[:zero_index]
                + "10"
                + bits[zero_index + 2:]
            )

            answer.append(int(bits, 2))

    return answer