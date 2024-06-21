
#Tạo hàm thông tin người dùng
def in_thong_tin_nguoi_dung(name, age):
    print(f"Xin chào, tôi là {name} và tôi {age} tuổi ")

ten_nguoi_dung = input("Nhập tên của bạn: ")
tuoi_nguoi_dung = input("Nhập tuổi của bạn: ")


try:
    tuoi_nguoi_dung = int(tuoi_nguoi_dung)
    in_thong_tin_nguoi_dung(ten_nguoi_dung, tuoi_nguoi_dung)
except ValueError:
    print("Lỗi: Tuổi phải là một số nguyên")
