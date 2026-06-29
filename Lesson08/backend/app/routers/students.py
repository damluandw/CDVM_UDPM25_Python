from fastapi import APIRouter, HTTPException, Depends
from typing import List
import pyodbc
from ..models import Student, StudentCreate, StudentUpdate
from ..database import get_db_connection

# Khởi tạo một Router dành riêng cho các API liên quan đến Sinh viên.
# prefix="/students": Tự động gắn tiền tố /students vào tất cả các URL bên dưới (đỡ phải gõ lặp lại).
# tags=["students"]: Giúp phân nhóm đẹp mắt trên giao diện tài liệu tự động (Swagger UI).
router = APIRouter(prefix="/students", tags=["students"])


# KỸ THUẬT DEPENDENCY INJECTION (Tiêm phụ thuộc)
# Hàm get_db() này sẽ cung cấp một đường kết nối CSDL (conn) cho mỗi lần người dùng gọi bất kỳ API nào,
# và cam kết đóng lại kết nối một cách an toàn (conn.close()) thông qua khối lệnh "finally".
def get_db():
    conn = get_db_connection()
    try:
        yield conn  # Lệnh "yield" sẽ tạm dừng hàm này và "nhường" đường kết nối cho hàm API phía dưới dùng
    finally:
        conn.close()  # Cho dù API bị sập hay lỗi thì hàm này vẫn bắt buộc phải chạy để dọn dẹp kết nối


# -------------------------------------------------------------
# 1. API: LẤY DANH SÁCH TOÀN BỘ SINH VIÊN (GET)
# response_model=List[Student]: Yêu cầu FastAPI kiểm tra và tự động định dạng dữ liệu trả về thành mảng [Student]
# -------------------------------------------------------------
@router.get("/", response_model=List[Student])
def read_students(db: pyodbc.Connection = Depends(get_db)):
    """Lấy danh sách tất cả sinh viên từ cơ sở dữ liệu SQL Server"""
    cursor = db.cursor()  # Mở con trỏ thực thi SQL
    cursor.execute("SELECT id, name, email, gpa FROM Students")  # Viết câu lệnh Select
    rows = cursor.fetchall()  # Nhặt toàn bộ dữ liệu mang về

    # Duyệt qua các dòng thô lấy được từ CSDL và biến chúng thành đối tượng Student (Python Model)
    students = []
    for row in rows:
        students.append(Student(id=row.id, name=row.name, email=row.email, gpa=row.gpa))

    return students


# -------------------------------------------------------------
# 2. API: THÊM MỚI MỘT SINH VIÊN (POST)
# -------------------------------------------------------------
@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: pyodbc.Connection = Depends(get_db)):
    """Thêm một sinh viên mới, trong quá trình thêm sẽ tự động phát hiện lỗi trùng lặp Email"""
    cursor = db.cursor()

    # Truy vấn kiểm tra xem email mà người dùng vừa nhập đã có ai xài trong DB hay chưa
    cursor.execute("SELECT id FROM Students WHERE email = ?", student.email)
    if cursor.fetchone():
        raise HTTPException(
            status_code=400, detail="Email đã tồn tại"
        )  # Nếu thấy, báo lỗi 400 (Dữ liệu không hợp lệ)

    try:
        # Thực thi lệnh INSERT.
        # Cú pháp "OUTPUT INSERTED.id" là đặc sản của SQL Server dùng để lấy ngay lập tức cái ID tự tăng vừa được tạo ra!
        cursor.execute(
            "INSERT INTO Students (name, email, gpa) OUTPUT INSERTED.id VALUES (?, ?, ?)",
            student.name,
            student.email,
            student.gpa,
        )
        new_id = cursor.fetchone()[0]  # Bắt lấy ID đó đưa vào biến new_id
        db.commit()  # Rất quan trọng: Xác nhận lưu thật sự xuống ổ cứng (CSDL)

        # Trả về đối tượng sinh viên vừa tạo kèm theo ID để giao diện Frontend đem đi hiển thị
        return Student(id=new_id, **student.model_dump())
    except Exception as e:
        db.rollback()  # Nếu gặp sự cố gì thì "quay ngược thời gian", hủy toàn bộ tác vụ vừa rồi
        raise HTTPException(status_code=500, detail=f"Lỗi thêm sinh viên: {str(e)}")


# -------------------------------------------------------------
# 3. API: CẬP NHẬT THÔNG TIN CỦA SINH VIÊN (PUT)
# -------------------------------------------------------------
@router.put("/{student_id}", response_model=Student)
def update_student(
    student_id: int, student: StudentUpdate, db: pyodbc.Connection = Depends(get_db)
):
    """Sửa thông tin của sinh viên thông qua mã ID"""
    cursor = db.cursor()

    # Bước 1: Trước khi muốn sửa ai đó, phải hỏi CSDL xem người đó có thực sự tồn tại không đã
    cursor.execute("SELECT id FROM Students WHERE id = ?", student_id)
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Sinh viên không tồn tại")

    # Bước 2: Nếu người dùng cố tình cập nhật Email sang một Email mới,
    # cần check xem email mới này có vô tình bị trùng với một sinh viên "khác" (tức id khác) không
    cursor.execute(
        "SELECT id FROM Students WHERE email = ? AND id != ?", student.email, student_id
    )
    if cursor.fetchone():
        raise HTTPException(
            status_code=400, detail="Email đã tồn tại ở một sinh viên khác"
        )

    try:
        # Chạy lệnh UPDATE kinh điển
        cursor.execute(
            "UPDATE Students SET name = ?, email = ?, gpa = ? WHERE id = ?",
            student.name,
            student.email,
            student.gpa,
            student_id,
        )
        db.commit()  # Lưu thay đổi
        return Student(id=student_id, **student.model_dump())
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Lỗi cập nhật sinh viên: {str(e)}")


# -------------------------------------------------------------
# 4. API: XÓA SINH VIÊN MÃI MÃI (DELETE)
# -------------------------------------------------------------
@router.delete("/{student_id}")
def delete_student(student_id: int, db: pyodbc.Connection = Depends(get_db)):
    """Xóa bỏ hoàn toàn sinh viên khỏi hệ thống bằng ID"""
    cursor = db.cursor()

    # Check nhanh xem ID truyền lên có tồn tại trong máy chủ chưa
    cursor.execute("SELECT id FROM Students WHERE id = ?", student_id)
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Sinh viên không tồn tại")

    try:
        # Tiễn sinh viên "lên đường"
        cursor.execute("DELETE FROM Students WHERE id = ?", student_id)
        db.commit()
        return {"message": "Xóa sinh viên thành công"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Lỗi xóa sinh viên: {str(e)}")
