## 流程控制

## if
a = [0, 1]

if a[0] > 0 and a[1] > 0:
    print("list a > 0")
elif a[0] > 0:
    print("list a[0] > 0")
elif a[1] > 0:
    print("list a[1] > 0")
else:
    print("list a < 0")

## for 循环 break 跳出循环
a = ["apple", "sfsd", "sdfsadf", "word", "sdfsdf"]
for ai in a:
    if ai == "word":
        print(ai)
        break

print("end")

## Case 1
list = [1, 2, 3, 4, 5]
ans = []

for ai in list:
    print(ai+1)
    s = [ai+1]
    print(s)
    ans = ans + s
print(ans)



