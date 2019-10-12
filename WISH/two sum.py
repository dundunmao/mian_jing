def two_sum(a, k ):
    hash = {}
    res = []
    for i in range(len(a)):
        if k - a[i] in hash:
            size = hash[k - a[i]]
            for ele in range(size):
                res.append([k - a[i], a[i]])
        if a[i] in hash:
            hash[a[i]] += 1
        else:
            hash[a[i]] = 1
    return res
a = [3,4,5,3,2,7]
print(two_sum(a, 7))
