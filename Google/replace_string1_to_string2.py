def replace(s1, s2):
    if len(s1) != len(s2):
        return False
    table = {}
    for i in range(len(s1)):
        if s1[i] not in table:
            table[s1[i]] = s2[i]
        else:
            if table[s1[i]] != s2[i]:
                return False


def replace2(s1, s2):
    if len(s1) != len(s2):
        return False
    table = {}
    for i in range(len(s1)):
        if s1[i] not in table:
            table[s1[i]] = s2[i]
        else:
            if table[s1[i]] != s2[i]:
                return False
    stack1 = []
    stack2 = []
    for ele in s2:
        if ele in table:
            stack1.append(ele)
        else:
            stack2.append(ele)
    res = stack2 + stack1
    return set(res)

if __name__ == "__main__":
    print(replace2('aabcc', 'ccdee'))
