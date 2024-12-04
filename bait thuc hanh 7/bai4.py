from itertools import islice

def file_read_from_head(fname, nlines):
    # Mở tệp và đọc n dòng đầu tiên
    with open(fname, 'r') as f:
        # Dùng islice để đọc n dòng đầu tiên từ tệp
        for line in islice(f, nlines):
            print(line, end='')  # in dòng ra mà không thêm ký tự newline dư thừa

