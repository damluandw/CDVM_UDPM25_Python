import os
import pyodbc
from dotenv import load_dotenv

# load_dotenv() tự động tìm file .env trong thư mục chứa code và nạp các biến môi trường vào hệ thống.
load_dotenv()

# Lấy chuỗi kết nối từ biến môi trường có tên "DB_CONNECTION_STRING".
# Nhờ cách này, nếu cấu hình CSDL bị thay đổi, ta chỉ cần sửa file .env mà không phải vào trong sửa source code.
CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")


def get_db_connection():
    """
    Hàm này có nhiệm vụ tạo và trả về đối tượng kết nối trực tiếp đến SQL Server.
    Mỗi khi một API (như lấy danh sách, thêm, sửa, xóa) cần giao tiếp với DB,
    nó sẽ gọi hàm này để xin một đường truyền kết nối.
    """
    try:
        # Sử dụng module pyodbc để mở kết nối dựa trên chuỗi cấu hình đã lấy được
        conn = pyodbc.connect(CONNECTION_STRING)
        return conn
    except pyodbc.Error as e:
        # Bắt lỗi nếu kết nối thất bại (sai mật khẩu, sai tên server, hoặc chưa bật máy chủ SQL Server)
        print("Lỗi kết nối cơ sở dữ liệu:", e)
        raise e
