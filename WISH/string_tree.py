def string_tree(a):
    res = []
    hash = []
    path = []
    for i in range(len(a[0])):
        path.append(a[0][i])
        row = 0
        dfs(a, row + 1, hash, path, res)
        path.pop()
    print(len(res))
    return res


def dfs(a, row, hash, path, res):
    if row == len(a):
        res.append(path[:])
    else:
        for i in range(len(a[row])):
            path.append(a[row][i])
            dfs(a, row + 1, hash, path, res)
            path.pop()

class StringTree:
    def string_tree(self, a):
        res = []
        hash = []
        path = []
        row = -1
        dfs(a, row + 1, hash, path, res)
        return res

    def dfs(self, a, row, hash, path, res):
        if row == len(a):
            res.append(path[:])
        else:
            for i in range(len(a[row])):
                path.append(a[row][i])
                dfs(self, a, row + 1, hash, path, res)
                path.pop()
a = ['hello', 'world', 'java']

a = ['af', 'bc', 'de']
x = StringTree()
assert(x.string_tree(a)==[['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'd'], ['a', 'c', 'e'], ['f', 'b', 'd'], ['f', 'b', 'e'], ['f', 'c', 'd'], ['f', 'c', 'e']])
print(string_tree(a))
