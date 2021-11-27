
## 计算器
print("计算器")
a = 2 + 2
b = (50 - 5*6) / 4

print(17 / 3, 17 // 3, int(17 / 3))
print(5 ** 2)
print(a, b)

w = 10
h = 2 * 2

print(w * h)

## 字符串
print("字符串\"")
s = "sbsadf"
s1 = s[:2] + "c" + s[3:len(s)]
print(s1)

## 列表
print("列表 list")
squares = [4, 1, 9, 16, 25]
squares.sort()
print(squares)
squares.reverse()
print(squares)
squares.append(10)
print(squares)
squares.pop()
print(squares)
a = squares.pop()
print(squares, a)
print()

squares2 = [squares, [1, 2, 3]]
print(squares2)
print(squares2[0][0])
print(squares2[1][2])