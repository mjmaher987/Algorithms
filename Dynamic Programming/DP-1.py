import math

if __name__ == '__main__':
    n = int(input())
    k = math.ceil(n / 2)

    mainArray = [[[math.inf for i1 in range(2)] for i2 in range(k + 1)] for i3 in range(3)]
    heights = list(map(int, input().split()))
    cost_afters = [0 for i in range(n)]
    costs = [0 for i in range(n)]
    for i in range(n):
        def cost(index):
            if index == 0:
                return 0
            return max(0, heights[index - 1] - heights[index] + 1)


        def cost_after(index):
            return max(0, heights[index] - heights[index - 1] + 1)


        costs[i] = cost(i)

        cost_afters[i] = cost_after(i)

    mainArray[0][0][0] = 0
    mainArray[0][1][1] = 0
    mainArray[1][0][0] = 0
    mainArray[1][1][0] = mainArray[0][1][1] + max(0, heights[1] - heights[1 - 1] + 1)
    mainArray[1][1][1] = max(0, heights[1 - 1] - heights[1] + 1)

    for i in range(3):
        mainArray[i][0][0] = 0

    for m1 in range(2, n):
        for t in range(1, min(k + 1, m1 + 2)):
            mainArray[m1 % 3][t][0] = min(mainArray[(m1 - 1) % 3][t][0],
                                          mainArray[(m1 - 1) % 3][t][1] + cost_afters[m1])

            mainArray[m1 % 3][t][1] = min(mainArray[(m1 - 1) % 3][t - 1][0] + costs[m1],
                                          mainArray[(m1 - 2) % 3][t - 1][1] + cost_afters[m1 - 1] + max(0, (
                                                  heights[m1 - 1] - cost_afters[m1 - 1]) - heights[m1] + 1),
                                          mainArray[(m1 - 2) % 3][t - 1][0] + costs[m1])

    last = ""
    for main_k in range(1, k + 1):
        first_answer = mainArray[(n - 1) % 3][main_k][0]
        second_answer = mainArray[(n - 1) % 3][main_k][1]
        main_answer = min(first_answer, second_answer)

        if main_answer == math.inf * (-1) or main_answer == math.inf:
            last += str('0 ')
        else:
            last += str(main_answer) + ' '
    print(last)
