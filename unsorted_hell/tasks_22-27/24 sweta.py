f=open("24-169.txt")
a=f.readline()

a=a.replace('XYZ','K')
a=a.replace('X',' ').replace('Y',' ').replace('Z',' ')

a=a.split()
print(len(max(a))*3)

