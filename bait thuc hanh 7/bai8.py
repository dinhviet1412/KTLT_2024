def write_list_to_file(fname, data_list):
    try:
        with open(fname, 'w', encoding='utf-8') as f:  # Mở tệp ở chế độ ghi ('w')
            for item in data_list:
                f.write(item + '\n')  # Ghi từng phần tử vào tệp, mỗi phần tử sẽ được ghi vào một dòng mới
        print(f"Đã ghi nội dung vào tệp {fname}.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
data = ["Dòng 1", "Dòng 2", "Dòng 3", "Dòng 4"]
file_name = 'output.txt'
write_list_to_file(file_name, data)
