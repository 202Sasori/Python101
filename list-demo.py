# List sử dụng để chứa 1 chuỗi giá trị
list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)
# Có thể lưu trữ nhiều biến khác nhau
list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), True]
print(list2)
print(type(list2))
# Hiển thị các giá trị trong List
print(list1[0])
print(list1[-1])
print(list1[3][0])
print(list1[3][-1])
# Thay đổi giá trị trong List
list1[0] = "X"
print(list1)
# Xóa giá trị trong List
del list1[0]
print(list1)
# Thêm giá trị vào List
list1.insert(0, "A")
print(list1)

del list1[0]
print(list1)
# Thêm giá trị vào List
list1 = ["A"] + list1
print(list1)

list1.append("G")
print(list1)
# Built in function
print(max(list1))
print(min(list1))
# Vị trí giá trị trong List
print(list1.index("C"))
print(list1[list1.index("C")])
# Đảo giá trị trong List
list1.reverse()
print(list1)

list1 = list1[::-1]
print(list1)
# Đếm số lượng giá trị xuất hiện trong List
print(list1.count("A"))
list1.append("A")
print(list1)
print(list1.count("A"))
# Xóa giá trị cuối List
list1.pop()
print(list1)
# Kết hợp giá trị 2 List
list3 = ["H", "I", "J"]
print(list3)

list1.extend(list3)
print(list1)
# Clear list
list1.clear()
print(list1)
# Sắp xếp giá trị trong List
list4 = [10, 12, 1, 0, 6, 2, 4]
print(list4)
# Tăng dần
list4.sort()
print(list4)
# Giảm dần
list4.sort(reverse=True)
print(list4)
# 2 List chỉ có thể kế thừa nhau
list5 = list4
print(list5)
print(list4)

list5[2] = "X"
print(list5)
print(list4)
# Copy giá trị từ list này sang list khác. Có thể thay đổi giá trị của list này mà không gây ảnh hưởng tới list được copy
list6 = list4.copy()
print(list4)
print(list6)

list6[2] = "A"
print(list6)
print(list4)
# Chuyển đổi kiểu dữ liệu trong list
list7 = ["1", "2", "3"]
print(list7)

list8 = list(map(float, list7))
print(list8)