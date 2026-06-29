-- Tạo cơ sở dữ liệu
CREATE DATABASE StudentHubDB;
GO

USE StudentHubDB;
GO

-- Tạo bảng Sinh Viên (Students)
CREATE TABLE Students (
    id INT IDENTITY(1,1) PRIMARY KEY, -- ID tự tăng
    name NVARCHAR(100) NOT NULL,      -- Họ và Tên sinh viên (hỗ trợ tiếng Việt)
    email VARCHAR(100) NOT NULL UNIQUE, -- Email, phải là duy nhất
    gpa DECIMAL(3,2) NOT NULL         -- Điểm GPA (Ví dụ: 3.60, 4.00)
);
GO

-- Thêm dữ liệu mẫu ban đầu (Mock Data từ file HTML)
INSERT INTO Students (name, email, gpa)
VALUES 
    (N'Nguyễn Hoàng Nam', 'nam.nh21@student.edu.vn', 3.6),
    (N'Trần Thị Khánh Huyền', 'huyen.ttk20@student.edu.vn', 3.9),
    (N'Lê Minh Triết', 'triet.lm22@student.edu.vn', 2.8),
    (N'Phạm Thảo Linh', 'linh.pt21@student.edu.vn', 3.4);
GO
