from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import students

# KHỞI TẠO ỨNG DỤNG FASTAPI
# Đây là "trái tim" của hệ thống Backend. Mọi cấu hình và chức năng đều được gắn vào biến 'app' này.
app = FastAPI(
    title="API Quản Lý Sinh Viên",  # Tên sẽ hiển thị tự động trên trang tài liệu API (Swagger UI ở đường dẫn /docs)
    description="RESTful API cho ứng dụng Quản Lý Sinh Viên dùng FastAPI và SQL Server",
)

# CẤU HÌNH BẢO MẬT CORS (Cross-Origin Resource Sharing)
# Mặc định, trình duyệt chặn các website (như file qlsv.html của bạn) kết nối tới một API chạy ở Port khác.
# Ta dùng đoạn code này để "cấp phép" cho Frontend được quyền gọi các lệnh GET/POST/PUT/DELETE tới Backend.
app.add_middleware(
    CORSMiddleware,
    # allow_origins: Ai được phép gọi? (Dấu "*" nghĩa là cho phép tất cả mọi trang web đều được gọi tới API này)
    # LƯU Ý: Khi đưa lên server thật, bạn nên thay dấu "*" bằng địa chỉ web chính thức của bạn để chống hacker.
    allow_origins=["*"],
    allow_credentials=True,  # Cho phép đính kèm Cookie/Token đăng nhập
    allow_methods=[
        "*"
    ],  # Cho phép mọi thao tác từ GET (lấy dữ liệu), POST (thêm), PUT (sửa) đến DELETE (xóa)
    allow_headers=["*"],  # Cho phép gửi mọi loại tiêu đề thông tin bổ sung (Header)
)

# KẾT NỐI ROUTER (Phân chia module)
# Thay vì viết hàng trăm dòng code xử lý Sinh Viên ngay tại file này cho rối mắt,
# ta đã viết chúng ở file routers/students.py rồi dùng hàm include_router() để "gắn" vào ứng dụng chính.
app.include_router(students.router)


# ENDPOINT TRANG CHỦ (Root Route)
# Giống như trang bìa của quyển sách. Khi mở http://127.0.0.1:8000/ trên trình duyệt,
# ứng dụng sẽ trả về dòng thông báo này giúp chúng ta biết Server đang chạy tốt.
@app.get("/")
def root():
    return {"message": "Hệ thống Quản lý Sinh viên API đang hoạt động!"}
