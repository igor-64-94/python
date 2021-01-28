
if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(*[e for e in nums if nums.count(e) == 1])