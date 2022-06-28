for i in range(1, 1000):
    n = bin(i)[2:]
    if n.count("1") > n.count("0"): n = n + "1"
    else: n += "0"
    if n.count("1") > n.count("0"): n = n + "1"
    else: n += "0"
    if int(n, 2)<57: print(int(n, 2))
