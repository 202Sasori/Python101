# STRING khai báo biến chứa dữ liệu là chuỗi
name = "nunu"
print(name)
# NUMER khai báo biến chứa dữ liệu là số
name_length = 6
print(name_length)
# Multiple assignment khai báo và gán giá trị nhiều biến nhiều giá trị cùng lúc
name, name_length = "nunu", 6
# Kiểm tra kiểu dữ liệu
print(type(name))
print(type(name_length))
# Ép kiểu
name_length = int("4")
print(type(name_length))

# Biến có phân biệt chữ hoa và chữ thường
name_length = 6
Name_length = 10

print(name_length)
print(Name_length)
# List
name_list = ["nunu", "zaka", "abc"]
print(type(name_list))

name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)

# Tuple
name_tuple = ('nunu', "kaza")
print(type(name_tuple))

# Dictionary
name_dictionary = {"nunu": 6, "hotax": 2}
print(type(name_dictionary))

# Boolean biến chứa giá trị logic true và false
name_boolean = True
print(type(name_boolean))

# Range
name_range = range(6)
print(type(name_range))

# Bytes
name_bytes = b"nunu02"
print(type(name_bytes))

# Hiển thị các biến vừa tạo
print(name_tuple)
print(name_list)
print(name_dictionary)
print(name_boolean)
print(name_range)
print(name_bytes)