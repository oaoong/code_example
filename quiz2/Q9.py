def solution(s):
    answer = len(s)
    length = len(s)
    for i in range(1, (length // 2) + 1):
        temp = ""
        count = 1
        for j in range(0, (length // i) * i, i):
            if (s[j:j + i] == s[j + i:j + 2 * i]):
                count += 1
            else:
                if (count >= 2):
                    temp = str(count) + temp + s[j:j + i]
                    count = 1
                else:
                    temp = temp + s[j:j + i]

        temp = temp + s[(length // i) * i:]
        answer = min(answer, len(temp))

    return answer