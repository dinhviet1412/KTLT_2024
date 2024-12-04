def file_read(fname):
    # Mở tệp với chế độ append để nối văn bản
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    
    # Mở tệp ở chế độ đọc và in ra nội dung tệp
    with open(fname, "r") as txt:
        print(txt.read())

# Ví dụ sử dụng
file_read('abc.txt')
