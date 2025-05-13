s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

shortest = s_list[0]

# วนลูปเปรียบเทียบกับสตริงตัวอื่น ๆ
for s in s_list[1:]:
    if len(s) < len(shortest):
        shortest = s

print("The shortest string:", shortest)
