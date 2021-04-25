import sqlite3
from mysql.connector import connect

# Kết nối với DB và MySQL
conn_db = sqlite3.connect('Furniture_Shop/du_lieu/ql_san_pham.db') # phải đi từ Furniture_Shop
conn_mysql = connect(
	host = 'localhost',
	port = '8889',
	user = 'root',
	passwd = 'root',
	database = 'ql_ban_hang'
)

# Đổ dữ liệu từ DanhMuc bên DB qua danh_muc bên MySQL
# chuoi_db = 'SELECT * FROM DanhMuc'
# kq = conn_db.execute(chuoi_db)
# for data in kq:
# 	chuoi_mysql = 'INSERT INTO danh_muc VALUES (%s, %s, %s)'
# 	cursor = conn_mysql.cursor()
# 	cursor.execute(chuoi_mysql, (data[0], data[1], data[2]))
# 	conn_mysql.commit()
# else:
# 	print('Done')


# Đổ dữ liệu từ SanPham ở DB vào san_pham bên MySQL
chuoi_db = 'SELECT * FROM SanPham'
run = conn_db.execute(chuoi_db)
for data in run:
	chuoi_mysql = 'INSERT INTO san_pham VALUES (%s, %s, %s, %s, %s, %s)'
	cursor = conn_mysql.cursor()
	cursor.execute(chuoi_mysql, (data[0], data[1], data[2], data[3], data[4], data[5]))
	conn_mysql.commit()
else:
	print('OK')

conn_db.close()
conn_mysql.close()