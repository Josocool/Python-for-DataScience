def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == number

numbers = [153, 370, 123, 9474, 8208]

for num in numbers:
    if is_armstrong(num):
        print(f"{num} เป็น Armstrong number !")
    else:
        print(f"{num} ไม่ใช่ Armstrong number !")
