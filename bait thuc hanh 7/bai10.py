def find_longest_words(text):
    # Tách văn bản thành danh sách các từ
    words = text.split()
    
    # Tìm độ dài của từ dài nhất
    max_length = max(len(word) for word in words)
    
    # Lọc ra các từ có độ dài bằng với max_length
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

# Ví dụ sử dụng
text = """
Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
"""
longest_words = find_longest_words(text)

print("Các từ dài nhất trong văn bản là:")
for word in longest_words:
    print(word)

