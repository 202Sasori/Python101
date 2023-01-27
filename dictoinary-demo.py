# Lưu giá trị với kiểu key:value
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(type(dict1))
print(len(dict1))
# Hiển thị, lấy giá trị trong dictionary
print(dict1["a"])
print(dict1.get("a"))
# Hiển thị, lấy giá trị chỉ định trong dictionary
print(dict1.keys())
print(dict1.values())
print(dict1.items())
# Giá trị không được trùng key
dict1["a"] = 1
print(dict1)
# Thêm giá trị
dict1["d"] = 4
print(dict1)
# Thay đổi giá trị
dict1["a"] = 0
print(dict1)
# Update giá trị
dict1.update({"a" : 1})
print(dict1)
# Xóa giá trị
dict1.pop("d")
print(dict1)

del dict1["c"]
print(dict1)
# Thêm dictionary vào dictionary
dict1["c"] = {"a": 1, "b": 2}
print(dict1)
# Dictionary rỗng
dict2 = {}
print(dict2)

dict3 = dict()
print(dict3)