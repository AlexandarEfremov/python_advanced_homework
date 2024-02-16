numbers = [int(x) for x in input().split()]


def cal_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]

    return numbers[idx] + cal_sum(nums, idx + 1)


print(cal_sum(numbers))
