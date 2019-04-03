def is_apple(tar, s, e):
    if e <= s:
        return False
    
    while s < e:
        if not tar[s] == tar[e]:
            return False
        
        s, e = s + 1, e - 1
    return True


def get_big_apple(s):
    if not s:
        return False
    
    res_tup = (0, 0)

    for index, val in enumerate(s):
        i, e = 0, index
        while i < e:
            res = is_apple(s, i, e)
            if res:
                if (e - i) > res_tup[1] - res_tup[0]:
                    res_tup = (i, e) 
            i += 1
    return s[res_tup[0]:res_tup[1] + 1]

if __name__ == '__main__':
    res = get_big_apple('abacdcaba')
    print(res)
