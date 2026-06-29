import uvicorn  # Import thư viện ASGI Server (người vận chuyển) để chạy ứng dụng FastAPI

# Kiểm tra: Chỉ chạy server khi ta trực tiếp thực thi file này (ví dụ: python run.py)
if __name__ == "__main__":
    
    # Cấu hình khởi chạy máy chủ:
    # 1. "app.main:app": Trỏ tới đối tượng 'app' bên trong file 'main.py' ở thư mục 'app'
    # 2. host="127.0.0.1": Server chỉ chạy trên máy cá nhân (Localhost), bảo mật khi lập trình
    # 3. port=8000: Mở cổng 8000 để nhận Request (URL truy cập sẽ là http://127.0.0.1:8000)
    # 4. reload=True: Tự động khởi động lại Server ngay lập tức mỗi khi bạn bấm Lưu code
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
