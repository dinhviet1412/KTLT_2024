def copy_file_manual(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as fsrc:
            with open(dst, 'w', encoding='utf-8') as fdst:
                # Đọc và ghi toàn bộ nội dung từ tệp src sang tệp dst
                content = fsrc.read()
                fdst.write(content)
        print(f"Đã sao chép nội dung từ {src} sang {dst}.")
    except FileNotFoundError:
        print(f"Tệp {src} không tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Ví dụ sử dụng
src_file = 'source.txt'
dst_file = 'destination.txt'
copy_file_manual(src_file, dst_file)
