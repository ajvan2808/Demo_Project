from flask import render_template, request, redirect, url_for
from Furniture_Shop import app

# Tạo biến chung
host = 'localhost'
port = '8889'
user = 'root'
passwd = 'root'

''' 
LAMP, WAMP, XAMPP, MAMP viết tắt của bộ ba phầm mềm Apache, MySQL và PHP
- Phần mềm giả lập server miễn phí, cho phép chạy thử website ngay trên máy tính cá nhân bằng Localhost.
- LAMP dùng cho hệ điều hành Linux, WAMP dùng cho Windows, MAMP dùng cho MacOS và Windows, XAMPP có thể dùng cho nhiều hệ điều hành
- Project này dùng MAMP

'''
