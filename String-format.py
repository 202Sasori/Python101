# Kiểu dữ liệu String
string1 = "String 1!"
string2 = 'String 2!'

print(string1)
print(string2)
# Cách dòng
string3 = """String 0003
.....
.....!"""

print(string3)
# Sử dụng kết hợp dấu ' và "
string4 = "I'am a string"
print(string4)
string5 = 'I"m a string'
print(string5)
# Chèn dấu " và cách dòng
string6 = "I\"m a string\nI\"am on newline!"
# Bytes string
string6 = "\\ \x41\x42\x43"
print(string6)
# Nhiều chuỗi giống nhau
string7 = "aaaaaaaaaa"
print(string7)

string7 = "a" * 10
print(string7)

print(len(string7))
# Kiểm tra chuỗi 4 có chứa 'nunu' hay không
print("nunu" in string4)
# Kiểm tra chuỗi 4 có bắt đầu bằng I hay không
print(string4.startswith("I"))
# Kiểm tra chuỗi 4 có bắt đầu bằng A hay không
print(string4.startswith("A"))
# Vị trí của chuỗi 'string' trong chuỗi 4
print(string4.index("string"))
# Viết hoa chuỗi
print(string4.upper())
# Viết thường chuỗi
print(string4.lower())
# Loại khoảng trắng
space_string = "Space,String!"
print(space_string)
print(space_string.strip())
# Thay đổi ký tự
print(space_string.replace("!","?").strip())
# Thay đổi chuỗi
print(space_string.replace("string","example"))
# Tách chuỗi
print(space_string.split(","))
print(space_string.split())
# Encode
string4 = "I am a string!"
print(string4)
print(string4.encode())
print(string4.encode("utf-8"))
# Căn lề trái cho chuỗi
print(string4.rjust(25))
print(string4.rjust(25,"X"))
# Căn lề phải cho chuỗi
print(string4.ljust(25))
print(string4.ljust(25,"X"))
# Hiển thị chuỗi
print("I am " + "a string")
print("String4 is " + str(len(string4)) + " characters long!")
# Cộng 2 số
print(1 + 1)
# Nối 2 chuỗi
print("1" + "1")
print(type("1" + "1"))
# Hiển thị chuỗi
print("string4 is {} characters long!".format(len(string4)))
# Hiển thị nhiều chuỗi
print("{} {} {}".format(len(string4), 5.0, 0x12))
# Thay đổi thứ tự hiển thị
print("{0} {2} {1}".format(len(string4), 5.0, 0x12))
print("{length}".format(length=len(string4)))
# Hiển thị độ dài strin4
length = len(string4)
print(f"string4 is {length} characters long!")
# Hiển thị độ dài string4
print("string4 is {length:.2f} characters long".format(length=len(string4)))
print("string4 is {length:.3f} characters long".format(length=len(string4)))
print("string4 is {length:.4f} characters long".format(length=len(string4)))
# Hiển thị độ dài string4 với kiểu Hex
print("string4 is {length:x} characters long".format(length=len(string4)))
# Hiển thị độ dài string4 với kiểu Binary
print("string4 is {length:b} characters long".format(length=len(string4)))
# Hiển thị độ dài string4 với kiểu Octal
print("string4 is {length:o} characters long".format(length=len(string4)))
# Hiển thị độ dài string4 với kiểu Int
print("string4 is %d characters long!" %len(string4))
# Hiển thị độ dài string4 với kiểu float
print("string4 is %f characters long!" %len(string4))
# Hiển thị độ dài string4 với kiểu Hex
print("string4 is %x characters long!" %len(string4))
