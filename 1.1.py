# Nhập số từ người dùng
number_str = input("Nhập một số: ")

#chuyển đổi chuỗi thành số nguyên
number = int(number_str)

# In ra số đã nhập
print("Số vừa nhập là: ", number)

# Thực hiện một số tác vụ với số vừa nhập
square = number ** 2
cube = number ** 3

#In ra kết quả 
print("Bình phương của", number, "là", square)
print("Lập phương của", number, "là", cube)
