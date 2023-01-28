# Function một khối code thực hiện một công việc nhất định có thể tái sử dụng lại nhiều lần
# Tạo function
def function1():
    print("Hello function!")
# Call function
function1()
function1()
# Return
def function2():
    return "Hello function2!"

return_from_function2 = function2()
print(return_from_function2)
# Function có toán tử
def function3(s):
    print("\t{}".format(s))

function3("parameter")
function3("parameter2")

def function4(s1, s2):
    print("{} {}".format(s1,s2))

function4("A", "B")
function4(s1="A", s2="B")
function4(s2="B", s1="A")

def function5(s1 = "default"):
    print("{}".format(s1))

function5()
function5("abc")
# Thêm toán tử tùy ý
def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6")
function6("function6", "a")
function6("function6", "a", "b", "c")

def function7(**ks):
    for a in ks:
        print(a, ks[a])

function7(a="1", b="2", c="3", d="4")
# Function có thể lưu nhiều kiểu tham số khác nhau
def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("string", 1.0, 1, ['a', 'b', 'c', 'd'])
# Global variable
v = 100
print(v)

def function9():
    global v
    v += 1
    print(v)

function9()
print(v)
# Đệ quy
def function10():
    print("function10")

def function11():
    function10()
    print("function11")

function11()

def function12(x):
    print(x)
    if x > 0:
        function12(x -1)

function12(5)

def function13(x):
    while x >= 0:
        print(x)
        x -= 1
function13(5)