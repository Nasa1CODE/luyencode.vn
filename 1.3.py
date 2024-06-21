# mở file txt
with open("file_goc.txt", "r",  encoding='utf-8') as file:
    content = file.read()


print("Nội dung file ban đầu:")
print(content)

lines = content.split("\n")
#loại bỏ dòng số 2
lines.pop(1)
content_edited = "\n".join(lines)

print("Nội dung sau khi loại bỏ dòng số 2: ")
print(content_edited)

#ghi nội dung sau khi chỉnh sửa vào file mới
with open("file_moi.txt", "w",  encoding='utf-8') as file:
    file.write(content_edited)
 
print("Đã tạo flie mới với nội dung đã chỉnh sửa.")