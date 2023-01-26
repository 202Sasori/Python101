# Toán tử logic
valid = True
not_valid = False

print(valid)
print(not_valid)

print(valid == True)
print(not_valid == True)

print(not valid)
print(not not_valid)
# Toán tử so sánh
print((10 < 9))
print((10 == 10))
print((10 != 10))
print((10 != 10))
print((10 >= 10))
print((10 <= 10))
print((10 > 9))

print("---------")
# and, or
print(10 > 5 and 10 < 5)
print( 10 > 5 or 10 < 5)

print(bool(0))
print(bool(1))

print(bool(0) == False)
print(bool(1) == True)
# Các phép toán
print(10 + 10)
print(10 - 10)
print(10 / 10)
print(10 // 10)

print(10 / 3)
print(10 // 3)

print(10 * 10)
print(10 ** 10)
print(10 % 10)

x = 10
print(x)
x = x + 1
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)

# Chuyển đổi nhị phân
x = 6
print(bin(x))
print(bin(x)[2:].rjust(4,"0"))
# Phép toán nhị phân &, |, >>, <<
y = 10
print(bin(y)[2:].rjust(4,"0"))
print(bin(x & y)[2:].rjust(4,"0"))
print(x & y)