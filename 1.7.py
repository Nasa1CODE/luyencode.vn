# even_numbers = []

# for num in range(4, 31):
#     #Kiểm tra số chẵn thì thêm vào danh sách
#     if num % 2 == 0:
#         even_numbers.append(num)


# # In ra các số chẵn
# print("Các số chẵn là ", even_numbers)


def tim_phan_tu_max(list):
    # Xử lý trường hợp danh sách rỗng
    if not list:
        return None
    

    #Giả sử phần tử đầu tiên là phần tử lớn nhất
    max_value = list[0]
    
    for so in list:
        if so > max_value:
            max_value = so
    return max_value

list = [4,5,7,10,2,4,15,6]
result = tim_phan_tu_max(list)
print("Phần tử có giá trị lớn nhất là: ", result)
