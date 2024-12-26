import csv
import sys
from Class.giao_dich import *
from Class.khach_hang import *
from Class.nguoi import *
from Class.nhan_vien import *
from Class.tai_khoan import *

class QuanLyKhachHang:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(QuanLyKhachHang, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.giao_dich_list = []
            self.khach_hang_list = []
            self.nguoi_list = []
            self.nhan_vien_list = []
            self.tai_khoan_list = []
            
            # Đọc dữ liệu từ các file CSV và lưu vào danh sách
            self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')
            self.doc_du_lieu_tu_file('Database/nhan_vien.csv', 'nhan_vien')
            self.doc_du_lieu_tu_file('Database/giao_dich.csv', 'giao_dich')
            self.doc_du_lieu_tu_file('Database/tai_khoan.csv', 'tai_khoan')
            self.doc_du_lieu_tu_file('Database/nguoi.csv', 'nguoi')  # Đọc dữ liệu từ file nguoi.csv
            
            self.initialized = True  # Đánh dấu đã khởi tạo dữ liệu

    def doc_du_lieu_tu_file(self, file_path, loai_du_lieu):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Bỏ qua dòng tiêu đề
                for row in reader:
                    if loai_du_lieu == 'khach_hang':
                        self.khach_hang_list.append(KhachHang(*row)) 
                    elif loai_du_lieu == 'nhan_vien':
                        self.nhan_vien_list.append(NhanVien(*row))
                    elif loai_du_lieu == 'giao_dich':
                        self.giao_dich_list.append(GiaoDich(*row))
                    elif loai_du_lieu == 'tai_khoan':
                        self.tai_khoan_list.append(TaiKhoan(*row))
                    elif loai_du_lieu == 'nguoi':
                        self.nguoi_list.append(Nguoi(*row))  # Giả sử có class Nguoi
        except FileNotFoundError:
            print(f"File {file_path} không tìm thấy database! Dừng ứng dụng.")
            sys.exit()
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file {file_path}: {e}")
            print("Dừng ứng dụng")
            sys.exit()

    def lam_moi_du_lieu(self):
        # Cập nhật lại dữ liệu từ database (file CSV) vào danh sách trong bộ nhớ
        self.giao_dich_list.clear()
        self.khach_hang_list.clear()
        self.nguoi_list.clear()
        self.nhan_vien_list.clear()
        self.tai_khoan_list.clear()
        
        # Đọc lại dữ liệu từ các file CSV và cập nhật lại danh sách
        self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')
        self.doc_du_lieu_tu_file('Database/nhan_vien.csv', 'nhan_vien')
        self.doc_du_lieu_tu_file('Database/giao_dich.csv', 'giao_dich')
        self.doc_du_lieu_tu_file('Database/tai_khoan.csv', 'tai_khoan')
        self.doc_du_lieu_tu_file('Database/nguoi.csv', 'nguoi')  # Đọc lại từ file nguoi.csv

    def luu_du_lieu_vao_file(self):
        try:
            with open('Database/khach_hang.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Khach_Hang', 'Ten', 'Dia_Chi', 'So_Dien_Thoai'])
                for kh in self.khach_hang_list:
                    writer.writerow([kh.ma_khach_hang, kh.ten, kh.dia_chi, kh.so_dien_thoai])

            with open('Database/nhan_vien.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Nhan_Vien', 'Ten', 'Chuc_Vu', 'Dia_Chi'])
                for nv in self.nhan_vien_list:
                    writer.writerow([nv.ma_nhan_vien, nv.ten, nv.chuc_vu, nv.dia_chi])

            with open('Database/giao_dich.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Giao_Dich', 'Ma_Khach_Hang', 'So_Tien', 'Ngay_Giao_Dich'])
                for gd in self.giao_dich_list:
                    writer.writerow([gd.ma_giao_dich, gd.ma_khach_hang, gd.so_tien, gd.ngay_giao_dich])

            with open('Database/tai_khoan.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Tai_Khoan', 'Ten_Tai_Khoan', 'So_Du'])
                for tk in self.tai_khoan_list:
                    writer.writerow([tk.ma_tai_khoan, tk.ten_tai_khoan, tk.so_du])

            # Lưu dữ liệu nguoi.csv
            with open('Database/nguoi.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Nguoi', 'Ten', 'Dia_Chi', 'So_Dien_Thoai'])
                for nguoi in self.nguoi_list:
                    writer.writerow([nguoi.ma_nguoi, nguoi.ten, nguoi.dia_chi, nguoi.so_dien_thoai])

            print("Dữ liệu đã được lưu vào các file CSV.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu dữ liệu vào file: {e}")
            
# Viết tất cả các hàm chức năng dưới này kèm comment
# [1]

# [2]

# [3]

# [4]

# [5]
