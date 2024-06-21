# def func1(*args):
#     for arg in args:
#         print(arg)

# func1(1, 2, 3)
# func1("Hello", "World")
def sun_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sun_recursive(n - 1)
    

result = sun_recursive(10)
print("Tổng các số từ 0 đến 10:", result)