def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    import sys
    print("http://cp1.nintendo.co.jp/" +
        lets_take_tea_break(*[int(i) for i in (argv[1], 17, 3569, 915)]))

