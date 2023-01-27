# Tuple khai báo giá trị có nhiều biến
# Biến chuỗi
tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))
# Biến số
tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))
# Lặp 
tuple_repeat = ('Repeat!') * 5
print(tuple_repeat)
print(type(tuple_repeat))
# Kết hợp nhiều kiểu dữ liệu
mixed_tuple = ("A", 6, ("B", 6))
print(mixed_tuple)
print(type(mixed_tuple))
# Kết hợp các tuple lại với nhau
tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))
# Gán biến cho giá trị trong tuple
item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)
# Kiểm tra tuple có chứa giá trị
print("item2" in tuple_items)
print("item4" in tuple_items)

# Vị trí của giá trị trong tuple
print(tuple_items.index("item2"))

# In thông tin biến
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])
# Độ dài của tuple
print(len(tuple_items))

# Hiển thị biến theo vị trí
# Vị trí cuối cùng
print(tuple_items[-1])
# Vị trí kế cuối
print(tuple_items[-2])
# Truy cập tuple
# Lấy giá trị từ index[0] đến index[2] (KHÔNG BAO GỒM index[2])
print(tuple_items[0:2])
print(tuple_items[:2])
# Lấy giá trị từ index[-3] đến index[-1] (KHÔNG BAO GỒM index[-1])
print(tuple_items[-3:-1])

string1 = "I am a string!"
print(string1[0:4])
print(string1[-1])