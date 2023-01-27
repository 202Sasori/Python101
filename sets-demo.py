# Set được dùng để lưu nhiều items trong một biến
# items có thứ tự, duy nhất và không thể thay đổi (có thể update và remove)
set1 = {"a", "b", "c"}
print(set1)
print(type(set1))

set2 = {"a", "a", "a"}
print(set2)
print(type(set2))

set3 = {"a", 0 , True}
print(set3)

set4 = set(("b", 1, False))
print(set4)
# Thêm dữ liệu vào set
set1.add("d")
print(set1)
# Update dữ liệu tron set
set3.update(set4)
print(set3)
# Set và List
list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

set5 = {4, 5, 6}
set6 = set4.union(set4)
print(set6)
# Xóa giá trị trong set
set4.discard(4)
print(set4)

set4.discard(4)
print(set4)

print(set1)
set1.pop()
print(set1)