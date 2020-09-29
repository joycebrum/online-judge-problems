def max_unique_subsequence(snowflakes, last_index):
    answer = 0
    i = 0
    for j in range(0, len(snowflakes)):
        key = snowflakes[j]
        i = max(i, last_index[key] + 1)
        answer = max(answer, j - i + 1)
        last_index[key] = j
    return answer

if __name__ == '__main__':
    test_case_number = int(sys.stdin.readline())
    last_index = {}
    for i in range(0, test_case_number):
        snowflakes_number = int(sys.stdin.readline())
        snowflakes = []
        last_index.clear()
        for j in range(0, snowflakes_number):
            snowflake = sys.stdin.readline().strip()
            snowflakes.append(snowflake)
            last_index[snowflake] = -1
        maximum = max_unique_subsequence(snowflakes, last_index)
        print(maximum)
