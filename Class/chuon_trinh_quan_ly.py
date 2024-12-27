import csv
import sys
import string
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
            self.nhan_vien_list = []
            self.tai_khoan_list = []
            self.nguoi_list = []
            
            # Đọc dữ liệu từ các file CSV và lưu vào danh sách
            self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')
            self.doc_du_lieu_tu_file('Database/nhan_vien.csv', 'nhan_vien')
            self.doc_du_lieu_tu_file('Database/giao_dich.csv', 'giao_dich')
            self.doc_du_lieu_tu_file('Database/tai_khoan.csv', 'tai_khoan')
            self.doc_du_lieu_tu_file('Database/nguoi.csv', 'nguoi')
            
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
                        self.nguoi_list.append(Nguoi(*row))
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
        #self.nhan_vien_list.clear()
        self.tai_khoan_list.clear()
        self.nguoi_list.clear()
        
        # Đọc lại dữ liệu từ các file CSV và cập nhật lại danh sách
        self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')
        self.doc_du_lieu_tu_file('Database/nhan_vien.csv', 'nhan_vien')
        self.doc_du_lieu_tu_file('Database/giao_dich.csv', 'giao_dich')
        #self.doc_du_lieu_tu_file('Database/tai_khoan.csv', 'tai_khoan')
        self.doc_du_lieu_tu_file('Database/nguoi.csv', 'nguoi')
    
    def luu_du_lieu_vao_file(self):
        try:
            # Lưu thông tin Người
            with open('Database/nguoi.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ho_Ten', 'Ngay_Sinh', 'Dia_Chi', 'So_Dien_Thoai', 'Email'])
                for nguoi in self.nguoi_list:
                    writer.writerow([nguoi.str_hoTen, nguoi.date_ngaySinh, nguoi.str_diaChi, nguoi.int_soDienThoai, nguoi.str_email])

            # Lưu thông tin Khách hàng
            with open('Database/khach_hang.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Khach_Hang', 'Hang_Khach_Hang', 'So_Tien_Da_Giao_Dich', 'So_Luong_Giao_Dich', 'Ngay_Tao_Tai_Khoan', 'Diem_Tich_Luy', 'So_Tien_Tiet_Kiem'])
                for kh in self.khach_hang_list:
                    writer.writerow([kh.str_maKhachHang, kh.bool_hangKhachHang, kh.str_soTienDaGiaoDich, kh.int_soLuongGiaoDich, kh.date_ngayTaoTaiKhoan, kh.int_diemTichLuy, kh.str_soTienTietKiem])

            # Lưu thông tin Tài khoản
            with open('Database/tai_khoan.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ten_Tai_Khoan', 'Mat_Khau', 'Ma_Nguoi_Dung', 'Tinh_Trang_Dang_Nhap', 'So_Lan_Da_Dang_Nhap'])
                for tk in self.tai_khoan_list:
                    writer.writerow([tk.str_tenTaiKhoan, tk.str_matKhau, tk.str_maNguoiDung, tk.bool_tinhTrangDangNhap, tk.int_soLanDaDangNhap])

            # Lưu thông tin Giao dịch
            with open('Database/giao_dich.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Ma_Giao_Dich', 'Ma_Khach_Hang', 'So_Tien_Thanh_Toan', 'Hanh_Khach_Di_Cung', 'Ngay_Giao_Dich',
                                 'Hinh_Thuc_Thanh_Toan', 'Trang_Thai_Thanh_Toan', 'Ten_Chuyen_Di', 'Gia_Chuyen_Di', 'Giam_Gia',
                                 'Do_Dai_Chuyen_Di', 'Dia_Diem_Tham_Quan', 'Ngay_Khoi_Hanh', 'So_Luong_Hanh_Khach', 'Thoi_Luong_Chuyen_Di',
                                 'Gia_Phong', 'Ten_Noi_O', 'Mo_Ta', 'Danh_Gia', 'Ten_Dia_Diem', 'Ten_Phuong_Tien', 'So_Luong_Cho_Ngoi',
                                 'Don_Vi_Cung_Cap'])
                for gd in self.giao_dich_list:
                    writer.writerow([gd.str_maGiaoDich, gd.str_maKhachHang, gd.str_soTienThanhToan, gd.arr_hanhKhachDiCung, gd.date_ngayGiaoDich,
                                     gd.bool_hinhThucThanhToan, gd.bool_trangThaiThanhToan, gd.str_tenChuyenDi, gd.string_giaChuyenDi, gd.str_giamGia,
                                     gd.int_doDaiChuyenDi, gd.arr_diaDiemThamQuan, gd.date_ngayKhoiHanh, gd.int_soLuongHanhKhach, gd.str_thoiLuongChuyenDi,
                                     gd.str_giaPhong, gd.str_tenNoiO, gd.str_moTa, gd.str_danhGia, gd.str_tenDiaDiem, gd.str_tenPhuongTien,
                                     gd.str_soLuongChoNgoi, gd.str_donViCungCap])

            print("Dữ liệu đã được lưu vào các file CSV.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu dữ liệu vào file: {e}")

            
# Viết tất cả các hàm chức năng dưới này kèm comment
# [1]

# [2]

# [3]

# [4]

# [5]
