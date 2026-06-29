from pydantic import BaseModel, EmailStr


# Lớp cơ sở (Base) định nghĩa các trường dữ liệu chung nhất của một Sinh Viên.
# BaseModel của thư viện Pydantic giúp tự động kiểm tra (validate) tính hợp lệ của kiểu dữ liệu đầu vào.
class StudentBase(BaseModel):
    name: str  # Tên bắt buộc là chữ (chuỗi string)
    email: EmailStr  # EmailStr tự động bắt lỗi nếu chuỗi nhập vào không đúng định dạng email (ví dụ gõ thiếu chữ @)
    gpa: float  # Điểm bắt buộc là số thập phân (float)


# Cấu trúc dùng khi người dùng gửi yêu cầu THÊM MỚI (POST) một sinh viên.
# Kế thừa toàn bộ từ StudentBase (cố tình không có trường id vì id do CSDL tự động sinh ra).
class StudentCreate(StudentBase):
    pass


# Cấu trúc dùng khi người dùng gửi yêu cầu CẬP NHẬT (PUT) thông tin một sinh viên.
class StudentUpdate(StudentBase):
    pass


# Cấu trúc dùng khi TRẢ DỮ LIỆU VỀ (Response) cho máy khách.
# Lúc này bắt buộc phải có thêm trường `id` (vì đã lấy dữ liệu thành công từ SQL Server).
class Student(StudentBase):
    id: int

    # Cấu hình from_attributes = True (ở Pydantic phiên bản cũ gọi là orm_mode = True)
    # Giúp tự động hiểu và "dịch" dữ liệu dạng Object (dòng dữ liệu thô từ DB) sang định dạng chuẩn JSON.
    class Config:
        from_attributes = True
