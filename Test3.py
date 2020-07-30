listA = []
for i in range(3, 30):
    if i % 3 == 0:
        listA.append(i)

print(listA)
try:
    print(test)
except Exception as e:
    print(str(e)+"这个错误需要修改")
