import sqlite3  # thư viện có sẵn trong python 3

conn = sqlite3.connect('employees.db') #trả về đối tượng conn dùng để tương tác với database SQLite student.db

cursor = conn.cursor() # trả về đối tượng cursor

# Tạo bảng
employees = """CREATE TABLE IF NOT EXISTS NHANVIEN (
    idNhanVien INTEGER PRIMARY KEY AUTOINCREMENT,
    tenNhanVien VARCHAR(255) unique not null, 
    cccd VARCHAR(255) unique not null, 
    email VARCHAR(255) unique not null, 
    phone VARCHAR(255) unique not null);"""

cursor.execute(employees) #Gửi các câu lệnh SQL đến database SQL


