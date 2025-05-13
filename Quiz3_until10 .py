
words = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

# ລຽງຄຳຕາມຄວາມຍາວ ຈາກນ້ອຍໄປຫຼາຍ
words.sort(key=len)

# ຫາຄວາມຍາວຂອງຄຳທີ່ສັ່ນທີ່ສຸດກ່ອນ (ຢູ່ຕົວທຳອິດຫຼັງລຽງແລ້ວ)
shortest_length = len(words[0])

# ເກັບຄຳທັ້ງໝົດທີ່ມີຄວາມຍາວເທົ່າກັບຄຳທີ່ສັ້ນທີ່ສຸດ
shortest_words = []
for word in words:
    if len(word) == shortest_length:
        shortest_words.append(word)

# ອາໄສ ', '.join(...) ເພື່ອລວມຄຳທັ້ງໝົດໃຫ້ເປັນຂໍ້ຄວາມດຽວ
result = ", ".join(f"'{w}'" for w in shortest_words)
print("The shortest string:", result)
