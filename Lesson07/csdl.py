import pyodbc

conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-O4BOPA7\SQL2022;DATABASE=QuanLySinhVien;Trusted_Connection=yes; TrustServerCertificate=yes;"
# conn = pyodbc.connect(conn_str)
# print("Kết nối thành công!")


with pyodbc.connect(conn_str) as conn:
    cursor = conn.cursor()
    # Thêm một sinh viên mới
    cursor.execute(
        "INSERT SinhVien ([MaSV], [HoTen], [NgaySinh], [GioiTinh], [MaLop]) VALUES  (?, ?, ?, ?, ?)",
        ("SV04", "Nguyễn Văn C", "20040623", "Nam", "UDPM2501"),
    )
    conn.commit()  # Quan trọng: Lưu thay đổi
