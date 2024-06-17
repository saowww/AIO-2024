def max_kernel(num_list, k):
    result = []
    loop_times = len(num_list)-k+1
    for i in range(loop_times):
        target_range = num_list[i:i+k]
        result.append(max(target_range))
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
