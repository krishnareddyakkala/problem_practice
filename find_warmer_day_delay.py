"""
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would
have to wait until a warmer temperature.
[73, 74, 75, 71, 70, 76, 72] -> [1, 1, 3, 2, 1, nothing, nothing]
"""


def find_warmer_day_delay(l):
    i = 0
    warmer_delay = [0] * len(l)
    while i+1 < len(l):
        if l[i]==l[i+1]:
            i += 1
            continue

        if l[i] < l[i+1]:
            warmer_delay[i] = 1
            i += 1
            continue

        j = i+1
        while l[i] > l[j]:
            j += 1
            if j >= len(l):
                break

        if j >= len(l):
            i += 1
            continue

        while i < j:
            warmer_delay[i] = j-i
            i += 1
    return warmer_delay


if __name__ == "__main__":
    l = [73, 74, 75, 71, 70, 76, 72]
    print find_warmer_day_delay(l)