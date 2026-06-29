class Xe:
    hang_xe = "Toyota"  # Thuộc tính lớp

    def __init__(self, mau, nam_san_xuat):
        self.mau = mau
        self.nam_san_xuat = nam_san_xuat


# Tạo object
xe1 = Xe("Đỏ", 2020)
xe2 = Xe("Xanh", 2023)

print(xe1.mau)  # → Đỏ
print(xe2.mau)  # → Xanh
