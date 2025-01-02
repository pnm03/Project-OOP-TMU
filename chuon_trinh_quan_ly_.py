import csv
import sys
import string
import random
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from Config.email_config import *
from Class.giao_dich import *
from Class.khach_hang import *
from Class.nhan_vien import *
from Class.tai_khoan import *
from Config.function import *

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
            
            

            
            # Đọc dữ liệu từ các file CSV và lưu vào danh sách
            self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')
            self.doc_du_lieu_tu_file('Database/nhan_vien.csv', 'nhan_vien')
            self.doc_du_lieu_tu_file('Database/giao_dich.csv', 'giao_dich')
            self.doc_du_lieu_tu_file('Database/tai_khoan.csv', 'tai_khoan')
            
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
        self.nhan_vien_list.clear()
        self.tai_khoan_list.clear()
        
        # Đọc lại dữ liệu từ các file CSV và cập nhật lại danh sách
        self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')
        self.doc_du_lieu_tu_file('Database/nhan_vien.csv', 'nhan_vien')
        self.doc_du_lieu_tu_file('Database/giao_dich.csv', 'giao_dich')
        self.doc_du_lieu_tu_file('Database/tai_khoan.csv', 'tai_khoan')
    
    def luu_du_lieu_vao_file(self):
        try:
            # Lưu thông tin Khách hàng (ghi tiếp)
            with open('Database/khach_hang.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Kiểm tra nếu file trống thì ghi tiêu đề
                if file.tell() == 0:
                    writer.writerow(['Ho_Ten', 'Ngay_Sinh', 'Dia_Chi', 'So_Dien_Thoai', 'Email', 'Ma_Khach_Hang', 
                                    'Hang_Khach_Hang', 'So_Tien_Da_Giao_Dich', 'So_Luong_Giao_Dich', 'Ngay_Tao_Tai_Khoan', 
                                    'Diem_Tich_Luy', 'So_Tien_Tiet_Kiem'])
                for kh in self.khach_hang_list:
                    writer.writerow([
                        kh.lay_thong_tin('str_hoTen'), 
                        kh.lay_thong_tin('date_ngaySinh'), 
                        kh.lay_thong_tin('str_diaChi'), 
                        kh.lay_thong_tin('int_soDienThoai'), 
                        kh.lay_thong_tin('str_email'), 
                        kh.lay_thong_tin('str_maKhachHang'), 
                        kh.lay_thong_tin('str_hangKhachHang'), 
                        kh.lay_thong_tin('str_soTienDaGiaoDich'), 
                        kh.lay_thong_tin('int_soLuongGiaoDich'), 
                        kh.lay_thong_tin('date_ngayTaoTaiKhoan'), 
                        kh.lay_thong_tin('int_diemTichLuy'), 
                        kh.lay_thong_tin('str_soTienTietKiem')
                    ])

            # Lưu thông tin Tài khoản (ghi tiếp)
            with open('Database/tai_khoan.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Kiểm tra nếu file trống thì ghi tiêu đề
                if file.tell() == 0:
                    writer.writerow(['Ten_Tai_Khoan', 'Mat_Khau', 'Ma_Nguoi_Dung', 'Tinh_Trang_Dang_Nhap', 'So_Lan_Da_Dang_Nhap'])
                for tk in self.tai_khoan_list:
                    writer.writerow([
                        tk.lay_thong_tin('str_tenTaiKhoan'), 
                        tk.lay_thong_tin('str_matKhau'), 
                        tk.lay_thong_tin('str_maNguoiDung'), 
                        tk.lay_thong_tin('bool_tinhTrangDangNhap'), 
                        tk.lay_thong_tin('int_soLanDaDangNhap')
                    ])
            # Lưu thông tin Giao dịch (ghi tiếp)
            with open('Database/giao_dich.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Kiểm tra nếu file trống thì ghi tiêu đề
                if file.tell() == 0:
                    writer.writerow(['Ma_Giao_Dich', 'Ma_Khach_Hang', 'So_Tien_Thanh_Toan', 'Hanh_Khach_Di_Cung', 'Ngay_Giao_Dich',
                                    'Hinh_Thuc_Thanh_Toan', 'Trang_Thai_Thanh_Toan', 'Ten_Chuyen_Di', 'Gia_Chuyen_Di', 
                                    'Giam_Gia', 'Do_Dai_Chuyen_Di', 'Dia_Diem_Tham_Quan', 'Ngay_Khoi_Hanh', 'So_Luong_Hanh_Khach', 
                                    'Thoi_Luong_Chuyen_Di', 'Gia_Phong', 'Ten_Noi_O', 'Mo_Ta', 'Danh_Gia', 'Ten_Dia_Diem', 
                                    'Ten_Phuong_Tien', 'So_Luong_Cho_Ngoi', 'Don_Vi_Cung_Cap'])
                    for gd in self.giao_dich_list:
                        writer.writerow([
                            gd.lay_thong_tin('str_maGiaoDich'), 
                            gd.lay_thong_tin('str_maKhachHang'), 
                            gd.lay_thong_tin('str_soTienThanhToan'), 
                            gd.lay_thong_tin('arr_hanhKhachDiCung'), 
                            gd.lay_thong_tin('date_ngayGiaoDich'),
                            gd.lay_thong_tin('str_hinhThucThanhToan'),
                            gd.lay_thong_tin('bool_trangThaiThanhToan'),
                            gd.lay_thong_tin('str_tenChuyenDi'), 
                            gd.lay_thong_tin('str_giaChuyenDi'), 
                            gd.lay_thong_tin('str_giamGia'), 
                            gd.lay_thong_tin('int_doDaiChuyenDi'), 
                            gd.lay_thong_tin('arr_diaDiemThamQuan'), 
                            gd.lay_thong_tin('date_ngayKhoiHanh'),
                            gd.lay_thong_tin('int_soLuongHanhKhach'),
                            gd.lay_thong_tin('str_thoiLuongChuyenDi'),
                            gd.lay_thong_tin('str_giaPhong'),
                            gd.lay_thong_tin('str_tenNoiO'),
                            gd.lay_thong_tin('str_moTa'),
                            gd.lay_thong_tin('str_danhGia'),
                            gd.lay_thong_tin('str_tenDiaDiem'),
                            gd.lay_thong_tin('str_tenPhuongTien'),
                            gd.lay_thong_tin('str_soLuongChoNgoi'),
                            gd.lay_thong_tin('str_donViCungCap')
                        ])
            in_thong_tin("", "Đã cập nhật cơ sở dữ liệu")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu dữ liệu vào file: {e}")


    # Menu
    def ChucNang_menu(self):
        in_thong_tin("M E N U", "1. Thêm khách\n2. Xóa khách hàng\n3. Tìm kiếm khách hàng\n4. Chỉnh sửa khách hàng\n5. Xem báo cáo\n6. Thoát chương trình")
        try:
            lua_chon = STR_nhap_trong_khung("Nhập lựa chọn của bạn", "Nhập từ 1 đến 6")
            if lua_chon == "1":
                clear_screen()
                self.ChucNang_them_khach_hang()
            elif lua_chon == "2":
                pass
            elif lua_chon == "6":
                clear_screen()
                sys.exit()
            else:
                clear_screen()
                in_thong_tin_loi("Lựa chọn không hợp lệ", "Vui lòng thao tác lại")
                tiep_tuc()
                clear_screen()
                self.ChucNang_them_khach_hang()
        except ValueError:
            in_thong_tin_loi("Lỗi", "Dừng chương trình")
            clear_screen()
            sys.exit()

    # Gửi mail
    def gui_mail(self, email, name, passwork):
        loading_spinner1(1)
        print()
        try:
            msg = MIMEText(f"""
Xin chào {name},

Chúng tôi gửi cho bạn thư xác nhận từ TRAVEL (Fake). Chúng tôi gửi cho bạn thông tin tài khoản. Bạn có thể đăng nhập tại "a.com" để kiểm tra thông tin chuyến đi cũng như các thông tin khác của mình.

Tài khoản: {email}
Mật khẩu: {passwork}

Trân trọng,
Đội ngũ TRAVEL (Fake)

Đây là thư thử nghiệm của phần mềm. Mọi thông tin đều là ảo. Vui lòng bỏ qua thư này.
    """)
            msg['Subject'] = 'Thông báo'
            msg['From'] = EMAIL_USERNAME
            msg['To'] = email

            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, email, msg.as_string())
            server.quit()
            in_thong_tin("", "Đã gửi mail thành công!")
        except smtplib.SMTPException as e:
            print(f"Lỗi gửi mail: {e}")
        except Exception as e:
            print(f"Lỗi hệ thống: {e}")

# Viết tất cả các hàm chức năng dưới này kèm comment
# [1]
    def ChucNang_them_khach_hang(self):
        in_thong_tin("MENU THÊM KHÁCH HÀNG", "1. Thêm khách hàng thủ công\n2. Thêm khách hàng bằng tệp có sẵn\n3. Trở về menu")
    
        try:
            lua_chon = STR_nhap_trong_khung("Nhập lựa chọn của bạn", "Nhập 1 hoặc 2")
            if lua_chon == "1":
                self.them_khach_hang_thu_cong()
            elif lua_chon == "2":
                clear_screen()
                in_thong_tin("", "THÊM KHÁCH HÀNG BẰNG FILE CSV")
                file_path = STR_nhap_trong_khung("Nhập đường dẫn tới file CSV", "Bỏ rỗng để quay lại")
                if (file_path == ""): 
                    clear_screen()
                    self.ChucNang_them_khach_hang()
                self.tao_moi_tai_khoan(file_path)
                tiep_tuc()
                clear_screen()
                self.ChucNang_them_khach_hang()
            elif lua_chon == "3":
                clear_screen()
                self.ChucNang_menu()
            else:
                clear_screen()
                in_thong_tin_loi("Lựa chọn không hợp lệ", "Vui lòng thao tác lại")
                tiep_tuc()
                clear_screen()
                self.ChucNang_them_khach_hang()
        except ValueError:
            in_thong_tin_loi("Lỗi", "Dừng chương trình")
            clear_screen()
            sys.exit()


    def them_khach_hang_thu_cong(self):
        try:
            clear_screen()
            in_thong_tin("", "THÊM KHÁCH HÀNG THỦ CÔNG")
            while True:
                str_hoTen = STR_nhap_trong_khung("Nhập họ tên", "Được phép có dấu")
                if (str_hoTen != ""):
                    break
                in_thong_tin_loi("Lỗi", "Vui lòng nhập đầy đủ họ tên")
            while True:
                date_ngaySinh = STR_nhap_trong_khung("Nhập ngày sinh", "YYYY-MM-DD")
                if BOOL_kiem_tra_ngay_sinh(date_ngaySinh):
                    break
                in_thong_tin_loi("Lỗi", "Ngày sinh không hợp lệ. Vui lòng nhập lại.")
            while True:
                str_diaChi = STR_nhap_trong_khung("Nhập địa chỉ", "Được phép có dấu")
                if (str_diaChi != ""):
                    break
                in_thong_tin_loi("Lỗi", "Vui lòng nhập đầy đủ địa chỉ")
            while True:
                int_soDienThoai = STR_nhap_trong_khung("Nhập số điện thoại", "Nhập số")
                if BOOL_kiem_tra_so_dien_thoai(int_soDienThoai):
                    break
                in_thong_tin_loi("Lỗi", "Số điện thoại không hợp lệ. Vui lòng nhập lại.")

            while True:
                str_email = STR_nhap_trong_khung("Nhập email", "abc@gmail.com")
                if BOOL_kiem_tra_email(str_email):
                    break
                in_thong_tin_loi("Lỗi", "Email không hợp lệ. Vui lòng nhập lại.")

            # Kiểm tra nếu khách hàng đã tồn tại trong database
            if self.kiem_tra_khach_hang_ton_tai(str_email, int_soDienThoai):
                in_thong_tin("Thông báo", f"Khách hàng với email {str_email} hoặc số điện thoại {int_soDienThoai} đã tồn tại")
                tiep_tuc()
                clear_screen()
                self.ChucNang_them_khach_hang()

            # Tạo mã khách hàng mới
            ma_khach_hang = self.STR_tao_moi_makhachhang()

            # Các trường thông tin khác (mặc định hoặc nhập thêm nếu cần)
            str_hangKhachHang = "Thường"  
            str_soTienDaGiaoDich = "0"
            int_soLuongGiaoDich = 0
            date_ngayTaoTaiKhoan = datetime.today().strftime('%Y-%m-%d')
            int_diemTichLuy = 0
            str_soTienTietKiem = "0"
            mat_khau = self.STR_tao_mat_khau()

            # Hiển thị thông tin để xác nhận
            clear_screen()
            in_thong_tin("XÁC NHẬN THÔNG TIN KHÁCH HÀNG", f"Họ tên: {str_hoTen}\nNgày sinh: {date_ngaySinh}\nĐịa chỉ: {str_diaChi}\nSố điện thoại: {int_soDienThoai}\nEmail: {str_email}\nMã khách hàng: {ma_khach_hang}\nMật khẩu tài khoản: {mat_khau}")
            
            xac_nhan = STR_nhap_trong_khung("Xác nhận lưu khách hàng này?", "Chọn co/khong")
            if xac_nhan.lower() != 'co':
                in_thong_tin("", "Hủy thao tác thêm khách hàng")
                self.lam_moi_du_lieu()
                tiep_tuc()
                clear_screen()
                self.ChucNang_them_khach_hang()

            # Tạo đối tượng khách hàng mới
            khach_hang = KhachHang(
                str_hoTen, date_ngaySinh, str_diaChi, int_soDienThoai, str_email, 
                ma_khach_hang, str_hangKhachHang, str_soTienDaGiaoDich, 
                int_soLuongGiaoDich, date_ngayTaoTaiKhoan, int_diemTichLuy, str_soTienTietKiem
            )
            self.khach_hang_list.append(khach_hang)

            # Tạo tài khoản mới cho khách hàng
            tai_khoan = TaiKhoan(
                str_email,     # Tên tài khoản (Email)
                mat_khau,      # Mật khẩu
                ma_khach_hang, # Mã khách hàng
                True,          # Tình trạng đăng nhập (mới tạo nên là True)
                0              # Số lần đã đăng nhập (0 khi mới tạo)
            )
            self.tai_khoan_list.append(tai_khoan)

            in_thong_tin("Thêm khách hàng thành công", f"Tài khoản đã được tạo với thông tin\nMã khách hàng: {ma_khach_hang}\nTàikhoản: {str_email}\nMật khẩu: {mat_khau}")
            xacNhanMail = STR_nhap_trong_khung("Bạn có muốn gửi mail tới khách hàng không?", "Chọn co/khong")
            if xacNhanMail != 'khong':
                self.gui_mail(str_email, str_hoTen, mat_khau)
            # Lưu lại dữ liệu vào file
            self.luu_du_lieu_vao_file()
            tiep_tuc()
            clear_screen()
            self.ChucNang_them_khach_hang()

        except Exception as e:
            print(f"Đã xảy ra lỗi khi thêm khách hàng bằng tay: {e}")


    def kiem_tra_khach_hang_ton_tai(self, email, so_dien_thoai):
        # Kiểm tra xem khách hàng đã tồn tại chưa
        for kh in self.khach_hang_list:
            if kh.lay_thong_tin("str_email") == email or kh.lay_thong_tin("int_soDienThoai") == so_dien_thoai:  # Email là phần tử thứ 4 và số điện thoại là thứ 5
                return True
        return False

    def STR_tao_moi_makhachhang(self):
        """Tạo mã khách hàng mới, giả sử là mã tự động tăng."""
        return f"KH{random.randint(10000, 99999)}"  # Tạo mã khách hàng ngẫu nhiên

    def tao_moi_tai_khoan(self, file_path):
        try:
            # Nhập thông tin từ file CSV của khách hàng và giao dịch
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Bỏ qua dòng tiêu đề
                thong_bao_them_tk = ""
                stt_tk = 1
                for row in reader:
                    str_hoTen, date_ngaySinh, str_diaChi, int_soDienThoai, str_email, \
                    str_hangKhachHang, str_soTienDaGiaoDich, int_soLuongGiaoDich, \
                    date_ngayTaoTaiKhoan, int_diemTichLuy, str_soTienTietKiem, str_maGiaoDich, \
                    str_soTienThanhToan, arr_hanhKhachDiCung, date_ngayGiaoDich, \
                    str_hinhThucThanhToan, bool_trangThaiThanhToan, str_tenChuyenDi, \
                    str_giaChuyenDi, str_giamGia, int_doDaiChuyenDi, arr_diaDiemThamQuan, \
                    date_ngayKhoiHanh, int_soLuongHanhKhach, str_thoiLuongChuyenDi, \
                    str_giaPhong, str_tenNoiO, str_moTa, str_danhGia, str_tenDiaDiem, \
                    str_tenPhuongTien, str_soLuongChoNgoi, str_donViCungCap = row

                    # Kiểm tra nếu khách hàng đã tồn tại trong database
                    if self.kiem_tra_khach_hang_ton_tai(str_email, int_soDienThoai):
                        in_thong_tin_loi("Cảnh báo", f"Khách hàng với email {str_email} hoặc số điện thoại {int_soDienThoai} đã tồn tại.")
                        continue  # Bỏ qua khách hàng này nếu đã tồn tại
                    # Tạo mật khẩu mới
                    mat_khau = self.STR_tao_mat_khau()
                    ma_khach_hang = self.STR_tao_moi_makhachhang()

                    # Xác nhận thêm mới khách hàng
                    in_thong_tin("XÁC NHẬN THÔNG TIN KHÁCH HÀNG", f"Họ tên: {str_hoTen}\nNgày sinh: {date_ngaySinh}\nĐịa chỉ: {str_diaChi}\nSố điện thoại: {int_soDienThoai}\nEmail: {str_email}\nMã khách hàng: {ma_khach_hang}\nMật khẩu tài khoản: {mat_khau}")
            
                    xac_nhan = STR_nhap_trong_khung("Xác nhận lưu khách hàng này?", "Chọn co/khong")
                    if xac_nhan.lower() != 'co':
                        in_thong_tin("", f"Hủy lưu khách hàng: {ma_khach_hang}")
                        continue
                    in_thong_tin("Thông báo", f"Đã xác nhân thêm khách hàng {ma_khach_hang}")
                    # Tạo tài khoản với thông tin đầy đủ
                    tai_khoan = TaiKhoan(
                        str_email,     # Tên tài khoản (Email)
                        mat_khau,      # Mật khẩu
                        ma_khach_hang,     # Sử dụng email làm mã khách hàng thay vì mã ngẫu nhiên
                        True,          # Tình trạng đăng nhập (mới tạo nên là True)
                        0              # Số lần đã đăng nhập (0 khi mới tạo)
                    )
                    self.tai_khoan_list.append(tai_khoan)

                    # Tạo đối tượng khách hàng mới
                    khach_hang = KhachHang(
                        str_hoTen, date_ngaySinh, str_diaChi, int_soDienThoai, str_email, 
                        ma_khach_hang, str_hangKhachHang, str_soTienDaGiaoDich, 
                        int_soLuongGiaoDich, date_ngayTaoTaiKhoan, int_diemTichLuy, str_soTienTietKiem
                    )
                    self.khach_hang_list.append(khach_hang)

                    # Tạo giao dịch mẫu (có thể thêm vào)
                    giao_dich = GiaoDich(
                        str_maGiaoDich, ma_khach_hang, str_soTienThanhToan, arr_hanhKhachDiCung, 
                        date_ngayGiaoDich, str_hinhThucThanhToan, bool_trangThaiThanhToan, str_tenChuyenDi,
                        str_giaChuyenDi, str_giamGia, int_doDaiChuyenDi, arr_diaDiemThamQuan, 
                        date_ngayKhoiHanh, int_soLuongHanhKhach, str_thoiLuongChuyenDi, str_giaPhong, 
                        str_tenNoiO, str_moTa, str_danhGia, str_tenDiaDiem, str_tenPhuongTien, 
                        str_soLuongChoNgoi, str_donViCungCap
                    )
                    self.giao_dich_list.append(giao_dich)
                    
                    
                    # Tạo thông báo các tài khoản được tạotạo
                    thong_bao_them_tk += f"[{stt_tk}] Tài khoản đã được tạo với\nMã khách hàng: {ma_khach_hang}\nTài khoản: {str_email}\nMật khẩu: {mat_khau}\n\n"
                    stt_tk += 1
                    xacNhanMail = STR_nhap_trong_khung(f"Bạn có muốn gửi mail tới khách hàng {ma_khach_hang} không?", "Chọn co/khong")
                    if xacNhanMail != 'khong':
                        self.gui_mail(str_email, str_hoTen, mat_khau)
                    # print(f"Tài khoản đã được tạo với mật khẩu: {mat_khau}")
                    # in_thong_tin()
                    

                # Lưu lại dữ liệu vào các file CSV
                tiep_tuc()
                clear_screen()
                if (stt_tk == 1):
                    in_thong_tin("Thông báo", "Không có khách hàng mới được thêm")
                    tiep_tuc()
                    clear_screen()
                    self.ChucNang_them_khach_hang()
                else:
                    in_thong_tin("Thông báo", thong_bao_them_tk)
                    self.luu_du_lieu_vao_file()
                    tiep_tuc()
                    clear_screen()
                    self.ChucNang_them_khach_hang()

        except Exception as e:
            clear_screen()
            in_thong_tin_loi(f"Đã xảy ra lỗi khi thêm user từ file {file_path}", "Vui lòng đảm bảo file đúng định dạng và có tồn tại")
            print(e)
            tiep_tuc()
            clear_screen()
            self.ChucNang_them_khach_hang()


    def STR_tao_moi_makhachhang(self):
        ma_khach_hang = random.randint(100, 999)
        while True:
            mkh = f"KH{ma_khach_hang}"
            if not any(a.lay_thong_tin("str_maKhachHang") == mkh for a in self.khach_hang_list):
                
                return mkh
            ma_khach_hang = random.randint(100, 999)
    def STR_tao_mat_khau(self, length=8):
        #Tạo mật khẩu ngẫu nhiên dài 8 ký tự gồm chữ và số.
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

# [2]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung

# [3]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung

# [4]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung

# [5]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung