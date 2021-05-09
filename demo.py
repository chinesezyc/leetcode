num='1234567'

def fetchCurValue(l, r):
    if l < r and num[l] == '0':
        return -1
    res = 0
    while l <= r:
        print(int(num[l]))
        a=int(num[l])
        res = res * 10 + int(num[l])
        l += 1
    return res


if __name__ == "__main__":
    ret = fetchCurValue(1,3)
    print(ret)