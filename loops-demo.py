# While loop
a = 1
while a < 5:
    a += 1
    print(a)

# For loop
for i in range(5):
    print(i + 6)

# Nest loop
for i in range(3):
    for j in range(3):
        print(i, j)
print("----")
# Loop control
# Break
for i in range(5):
    if i == 2:
        break
    print(i)
# Continue
print("----")
for i in range(5):
    if i == 2:
        continue
    print(i)
# Pass
print("----")
for i in range(5):
    if i == 2:
        pass
    print(i)
print("----")
# Loop throught string
for c in "string":
    print(c)
print("----")
# Loop throught dictionary
for key , value in {"a": 1, "b": 2, "c": 3}.items():
    print(key, value)