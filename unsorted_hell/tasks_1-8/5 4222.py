for i in range(1, 100000):
    n = hex(i//2)[2:]
    if i%4 != 0: n = "F"+n+"A0"
    else: n = "15"+n+"C"
    n = int(n, 16)
    if n < 65536: print(i)
