# khai báo biến toàn cục
so_du = 1000

# def rut_tien(so_tien):
#     global so_du
#     if so_tien > so_du:
#         print("Số dư không đủ để rút tiền.")
#     else:
#         so_du -= so_tien
#         print(f"Bạn đã rút {so_tien} đồng. Số dư còn lại: {so_du} đồng.")


def rut_tien(so_tien):
    tien_rut = int(input("Số tiền bạn muốn rút: "))
    if tien_rut > so_tien:
        print("Số dư không đủ để rút tiền.")
    else:
        so_tien -= tien_rut
        print(f"Bạn đã rút {tien_rut} đồng. Số dư còn lại: {so_tien} đồng.")
    return so_tien


# Gọi hàm để rút tiền
so_du = rut_tien(so_du)
print(f"Số dư cuối cùng: {so_du} đồng.")
