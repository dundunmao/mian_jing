import collections
def add_two_array(a, b):
    n = len(a)
    m = len(b)
    i = n - 1
    j = m - 1
    res = collections.deque()
    while i >= 0 and j >= 0:
        cur = a[i] + b[j]
        res.appendleft(str(cur))
        i -= 1
        j -= 1
    while i >= 0:
        res.appendleft(str(a[i]))
        i -= 1
    while j >= 0:
        res.appendleft(str(b[j]))
        j -= 1
    return [int(ele) for ele in ''.join(res)]
a =  [1, 0 , 9]
b = [90, 788, 100, 5]
func = add_two_array(a, b)
assert (func == [9,0,7,8,9,1,0,0,1,4])

a =  [3,5,7]
b = [6,4]
func = add_two_array(a, b)
assert (func == [3,1,1,1,1])
