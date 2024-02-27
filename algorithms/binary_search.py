array = [int(x) for x in input().split()]
searched_num = int(input())


def binary_search(arr, num):
    current_arr = arr
    mid_point = current_arr // 2
    
