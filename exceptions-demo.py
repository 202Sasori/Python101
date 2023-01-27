# Try except
try:
    f = open("asdfhjk")
except:
    print("Something was wrong!")

try:
    f = open("top-10.txt")
except FileNotFoundError:
    print("File does not exist!")
except Exception as e:
    print(e)
finally:
    print("This message!")

n = 100
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be an int!")

print(1/n)

n = 0
assert(n != 0)
print(1/n)