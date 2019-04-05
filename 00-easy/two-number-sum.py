def twoNumberSum1(array, targetSum):
    for i, n in enumerate(array):
        for j in range(i + 1, len(array)):
            a = array[i]
            b = array[j]
            if a + b == targetSum:
                return sorted([a, b])
    return []


def twoNumberSum2(array, targetSum):
    s = set(array)
    for x in array:
        y = targetSum - x
        if x != y and y in s:
            return sorted([x, y])
    return []
