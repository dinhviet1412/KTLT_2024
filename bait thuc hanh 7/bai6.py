import os

def file_read_from_tail(fname, lines):
    bufsize = 8192  # Đọc dữ liệu theo từng khối 8KB
    fsize = os.stat(fname).st_size  # Lấy kích thước tệp
    iter = 0
    data = []
    
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize  # Nếu kích thước tệp nhỏ hơn bufsize, chỉ đọc hết tệp
        while True:
            iter += 1
            f.seek(fsize - bufsize * iter)  # Di chuyển con trỏ đến vị trí thích hợp trong tệp
            data.extend(f.readlines())  # Đọc các dòng vào list 'data'
            
            if len(data) >= lines or f.tell() == 0:  # Nếu đã đọc đủ số dòng yêu cầu hoặc hết tệp
                print(''.join(data[-lines:]))  # In ra n dòng cuối cùng
                break

# Ví dụ sử dụng
file_read_from_tail('test.txt', 2)
