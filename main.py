min = 10 ** 10

for i in range(2222, -1, -1):
    s = str(i)
    flag = True
    for j in range(len(s)):
        if (s[j] == s[len(s) - j - 1]):
            continue
        else:
            flag = False
    if flag == True:
        print(i)

