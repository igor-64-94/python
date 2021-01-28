
if __name__ == '__main__':
    nums = list(map(int, input().split()))
    new_nums = [nums[i] for i in range(1, len(nums)) if nums[i] > nums[i-1]]
    print(*new_nums)