def prost(n):
    return all(n%x != 0 for x in range(2, int(n**0.5) + 1))
colv = 0
curr = 10_000_000
while colv != 3:
    if prost(curr - 1):
        print(10_000_000 - curr + 1, curr - 1)
        colv += 1
    curr -= 1
colv = 0
curr = 10_000_000
while colv != 3:
    if prost(curr + 1):
        print(curr + 1 - 10_000_000, curr + 1)
        colv += 1
    curr += 1
    
