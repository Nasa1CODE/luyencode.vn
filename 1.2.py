# pi = 3.14159
# number = format(pi, ".2f")
# print(number)
user_input = input("Nhập danh sách 5 số float, cách nhau bằng dấu phẩy: ")
input_list = user_input.split(",")

numbers = []

for num in input_list:
    try:
        float_num = float(format(float(num), ".2f"))
        numbers.append(float_num)
    except ValueError:
        print(f"{num} không phải là một số float hợp lệ")


if len(numbers) == 5:
    try:
        sum_nums = sum(numbers)
        average = format(sum(numbers)/ len(numbers), ".2f")
        max_num = max(numbers)
        min_num = min(numbers)

        print("Danh sách số float:")
        print(numbers)
        print("Tổng: ", sum_nums)
        print("Trung bình: ", type(average))
        print("Giá trị lớn nhất: ", max_num)
        print("Giá trị nhỏ nhất: ", min_num)
    except ValueError as e:
        print("Lỗi", e)
else:
    print("Vui lòng nhập chính xác 5 số float.")