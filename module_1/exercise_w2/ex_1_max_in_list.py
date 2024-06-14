def max_kernel(user,k):
    output =[]
    for i in range(len(user)-k +1):
        ls = []
        for j in user[i:i+k]:
            ls.append(j)
        output.append(max(ls))
    return output
num_list = [3,4,5,1,-44,5,10,12,33,1]
k = 3
print(max_kernel(num_list,k))
