def red_green(a):

    max_diff = 0
    min_diff_from_begin = 0
    start = -1
    end = 0
    count_zero = 0
    count_one = 0
    res = [start, end]
    for i in range(len(a)):
        if a[i] == 0:
            count_zero += 1
        else:
            count_one += 1
        diff_from_begin = count_one - count_zero
        if diff_from_begin - min_diff_from_begin > max_diff:
            max_diff = diff_from_begin - min_diff_from_begin
            res = [start + 1, i]
        if diff_from_begin < min_diff_from_begin:
            start = i
            min_diff_from_begin = diff_from_begin
    return res

a = [1,0,0,1,0] #[0, 0]
print(red_green(a))
a = [1,1,0,0,1,0] # [0, 1]
print(red_green(a))
a = [1,1,0,1,1,1] # [0, 5]
print(red_green(a))
a = [0, 1,1,0,1,1] # [1, 5]
print(red_green(a))
a = [0,0, 1,0,1,0,0,1,1,1] # [7, 9]
print(red_green(a))
