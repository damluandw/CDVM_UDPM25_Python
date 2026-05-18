# Bài tập 1:
ho_ten = input("Nhập họ tên của bạn: ")
print("Xin chào, " + ho_ten)
# Bài tập 2:
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tong = a + b
hieu = a - b
tich = a * b
print("Tổng: ", tong)
print("Hiệu: ", hieu)
print("Tích: ", tich)
if b != 0:
    thuong = a / b
    print("Thương: ", thuong)
else:
    print("Không thể chia cho 0")

# Bài tập 3: Giải phương trình bậc nhất ax + b = 0
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a != 0:
    x = -b / a
    print("Nghiệm của phương trình là: x =", x)
elif b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Phương trình vô nghiệm")

# Bài tâp 4: Giải phuơng trình bậc hai ax^2 + bx + c = 0
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4 * a * c
if delta > 0:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print("Phương trình có hai nghiệm phân biệt: x1 =", x1, "và x2 =", x2)
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép: x =", x)
else:
    print("Phương trình vô nghiệm")

# Bài tâp 5: In ra các số từ 1 đến số vừa nhập
n = int(input("Nhập n: "))
# Cách 1
for i in range(n):
    print(i + 1, end=", ")
# Cách 2
for i in range(1, n + 1):
    print(i, end=", ")
print()  # in xuống dòng sau khi in xong các số
# cách 3:
i = 1
while True:
    print(i, end=", ")
    i += 1
    if i >= n:
        break
print()
# Cách 4:
i = 1
while i <= n:
    print(i, end=", ")
    i += 1
print()
# Bài tập 6: In ra các số chẵn
n = int(input("Nhập số n: "))
# Cách 1
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=", ")
print()
# Cách 2:
for i in range(1, n + 1):
    if i % 2 != 0:
        continue
    print(i, end=", ")
print()
# Cách 3:
for i in range(2, n + 1, 2):
    print(i, end=", ")
print()
# Bài tập 7:
n = int(input("Nhập số n: "))
for i in range(1, n + 1, 3):
    print(i, end=", ")
print()
# Bài tập 8: In số nguyên tố
n = int(input("Nhập số n: "))
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=", ")
