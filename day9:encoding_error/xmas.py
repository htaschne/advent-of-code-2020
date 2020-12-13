
import sys

def checkout(curr, value):
    s = sum(curr)
    if s == value:
        print(max(curr) + min(curr))
        exit(0)

def two(value, nums):
    n = len(nums)
    for size in range(2, n):
        curr = []
        it = 0
        while len(curr) != size:
            curr.append(nums[it])
            it += 1

        checkout(curr, value)

        while it < n:
            curr.pop(0)
            curr.append(nums[it])
            checkout(curr, value)
            it += 1


def check(curr, nums, i):
    for j in range(len(curr)):
        for k in range(j+1, len(curr)):
            if curr[j] + curr[k] == nums[i]:
                return True
    return False;

def main():
    nums = [int(line.rstrip()) for line in open(sys.argv[1]).readlines()]

    curr = []

    for i in range(25):
        curr.append(nums[i])

    for i in range(25, len(nums)):
        ok = check(curr, nums, i)
        if not ok:
            print(nums[i])
            two(nums[i], nums)
            exit(0)

        curr.pop(0)
        curr.append(nums[i])


main()
