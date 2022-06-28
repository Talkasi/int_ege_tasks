s = open('24-153.txt').readline().split('D')
print(len(min([x for x in s if x != ''], key = len)) + 2)
