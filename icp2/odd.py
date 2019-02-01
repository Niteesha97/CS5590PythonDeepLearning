list = []
for i in range(100, 500):
    num = str(i)
    if (int(num[0])%2!=0) and (int(num[1])%2!=0) and (int(num[2])%2!=0):
        list.append(num)
print( ",".join(list))