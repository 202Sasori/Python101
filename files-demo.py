# Mở file
f = open('top-10.txt')
print(f)
# Chọn mode cho file
f = open('top-10.txt','rt')
print(f)
# Đọc file 
print(f.readline())
print(f.readline())

f.seek(0)
print(f.readline())

f.seek(0)
for line in f:
    print(line.strip())

f.close()
# Viết file
f = open("test.txt", "a")
f.write("test line two!")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

