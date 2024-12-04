# Mở tệp văn bản và đọc nội dung
file_path = 'ten_tap_tin.txt'  # Đường dẫn tệp văn bản

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # Đọc toàn bộ nội dung tệp
        print(content)  # In ra nội dung tệp
except FileNotFoundError:
    print(f"Tệp {file_path} không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
