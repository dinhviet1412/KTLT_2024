# Hàm đếm số dòng trong tệp văn bản
def count_lines(file_path):
    try:
        # Mở tệp ở chế độ đọc
        with open(file_path, 'r') as file:
            # Đọc tất cả các dòng trong tệp và đếm số dòng
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "Tệp không tồn tại."

# Nhập đường dẫn tệp từ người dùng
file_path = input("Nhập đường dẫn tệp văn bản: ")

# Gọi hàm và in kết quả
result = count_lines(file_path)
print(f"Số dòng trong tệp là: {result}")
