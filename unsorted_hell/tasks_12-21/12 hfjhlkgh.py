s = 29*"5" + 6 * "4" + "43" * 17
print(s.count("3"), s.count("4"), s.count("5"))
while "43" in s or "53" in s:
    if "43" in s:
        s = s.replace("43", "33", 1)
    else:
        s = s.replace("53", "433", 1)

print(s)
print(s.count("3"))
