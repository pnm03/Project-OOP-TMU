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
            self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/khach_hang.csv', 'khach_hang')
            self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/nhan_vien.csv', 'nhan_vien')
            self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/giao_dich.csv', 'giao_dich')
            self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/tai_khoan.csv', 'tai_khoan')
            
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
        self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/khach_hang.csv', 'khach_hang')
        self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/nhan_vien.csv', 'nhan_vien')
        self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/giao_dich.csv', 'giao_dich')
        self.doc_du_lieu_tu_file('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/tai_khoan.csv', 'tai_khoan')
    
    def luu_du_lieu_vao_file(self):
        try:
            # Lưu thông tin Khách hàng (ghi tiếp)
            with open('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/khach_hang.csv', mode='w', newline='', encoding='utf-8') as file:
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
            with open('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/tai_khoan.csv', mode='w', newline='', encoding='utf-8') as file:
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
            with open('E:/Project-OOP-TMU-main (8)/Project-OOP-TMU-main/Database/giao_dich.csv', mode='w', newline='', encoding='utf-8') as file:
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

    def kiem_tra_dang_nhap(self):
        in_thong_tin("ĐĂNG NHẬP", "Nhập thông tin tài khoản, mật khẩu để đăng nhập")
        while True:
            ten_tai_khoan = STR_nhap_trong_khung("Tên tài khoản", "Nhập tên tài khoản").strip()
            mat_khau = STR_nhap_trong_khung("Mật khẩu", "Nhập mật khẩu").strip()

            for tai_khoan in self.tai_khoan_list:
                if tai_khoan.lay_thong_tin("str_tenTaiKhoan") == ten_tai_khoan:
                    if not tai_khoan.lay_thong_tin("bool_tinhTrangDangNhap"):
                        in_thong_tin_loi("Đăng nhập thất bại", "Tài khoản đã bị khóa.")
                        tiep_tuc()
                        clear_screen()
                        return
                    if tai_khoan.lay_thong_tin("int_soLanDaDangNhap") >= 3:
                        in_thong_tin_loi("Cảnh báo", "Tài khoản đã bị khóa do nhập sai mật khẩu quá 3 lần.")
                        tai_khoan.chinhSuaThongTin(tinh_trang_dang_nhap=False)
                        self.luu_du_lieu_vao_file()  # Cập nhật dữ liệu vào file
                        tiep_tuc()
                        clear_screen()
                        return
                    if tai_khoan.Bool_kiemTraMatKhau(ten_tai_khoan, mat_khau):
                        in_thong_tin("Đăng nhập thành công", "Chúc mừng bạn đã đăng nhập thành công.")
                        tai_khoan.reset_so_lan_dang_nhap_sai()
                        self.luu_du_lieu_vao_file()  # Lưu lại thay đổi vào file
                        tiep_tuc()
                        clear_screen()
                        ma_nguoi_dung = tai_khoan.lay_thong_tin("str_maNguoiDung")

                            # Nếu là nhân viên (NV), chuyển đến menu chức năng
                        if "NV" in ma_nguoi_dung:# kiểm tra mã người dùng
                                self.ChucNang_menu()  # Chuyển đến menu chức năng cho nhân viên
                                break                       
                            # Nếu là khách hàng (KH), hiển thị tùy chọn đổi mật khẩu hoặc đăng xuất
                        elif "KH" in ma_nguoi_dung:
                            while True:
                                in_thong_tin("Lựa chọn","1. Đổi mật khẩu\n2. Đăng xuất")
                                lua_chon = STR_nhap_trong_khung("","Nhập lựa chọn 1 hoặc 2").strip()
                                tiep_tuc()
                                clear_screen()
                                if lua_chon == "1":
                                    mat_khau_moi = STR_nhap_trong_khung("Mật khẩu", "Nhập mật khẩu mới: ").strip()                                
                                    tai_khoan.chinhSuaThongTin(mat_khau=mat_khau_moi)
                                    in_thong_tin("Thông báo", "Mật khẩu đã được đổi thành công.")
                                    self.luu_du_lieu_vao_file()  # Lưu lại thay đổi vào file
                                    break
                                elif lua_chon == "2":
                                    in_thong_tin("Thông báo", "Đăng xuất.")
                                    sys.exit()
                                else:
                                    in_thong_tin_loi("Lỗi", "Lựa chọn không hợp lệ. Vui lòng thử lại.")
                            return 
                    else:
                        in_thong_tin_loi("Đăng nhập thất bại", "Sai mật khẩu. Vui lòng thử lại.")
                        tai_khoan.chinhSuaThongTin(so_lan_da_dang_nhap=tai_khoan.lay_thong_tin("int_soLanDaDangNhap")+1)
                        self.luu_du_lieu_vao_file()  # Lưu lại thay đổi vào file
                        chon=STR_nhap_trong_khung("Bạn muốn thử lại không?", "Nhập c(có), k(không)")
                        if chon == "k":
                            in_thong_tin("", "Đã hủy đăng nhập")
                            tiep_tuc()
                            clear_screen()
                            sys.exit()
                        else:
                            tiep_tuc()
                            clear_screen()
                            if tai_khoan.lay_thong_tin("int_soLanDaDangNhap") == 3:
                                in_thong_tin_loi("Cảnh báo", "Tài khoản đã bị khóa do nhập sai mật khẩu quá 3 lần.")
                                tai_khoan.chinhSuaThongTin(tinh_trang_dang_nhap=False)
                                self.luu_du_lieu_vao_file()  # Cập nhật dữ liệu vào file
                                tiep_tuc()
                                clear_screen()
                                sys.exit()
                           
                            if tai_khoan.lay_thong_tin("int_soLanDaDangNhap") == 2:
                                in_thong_tin_loi("Cảnh báo", "Bạn chỉ còn 1 lần đăng nhập.")
                                self.kiem_tra_dang_nhap()
                     
    # Menu CN
    def ChucNang_menu(self):
        in_thong_tin("M E N U", "1. Thêm khách\n2. Xóa khách hàng\n3. Tìm kiếm khách hàng\n4. Chỉnh sửa khách hàng\n5. Xem báo cáo\n6. Đăng xuất")
        try:
            lua_chon = STR_nhap_trong_khung("Nhập lựa chọn của bạn", "Nhập từ 1 đến 6")
            if lua_chon == "1":
                clear_screen()
                self.ChucNang_them_khach_hang()
            elif lua_chon == "2":
                clear_screen()
                self.ChucNang_xoa_khach_hang()
            elif lua_chon == "3":
                clear_screen()
                self.ChucNang_tim_kiem_khach_hang()
            elif lua_chon == "4":
                clear_screen()
                self.ChucNang_chinh_sua_khach_hang()
            elif lua_chon == "5":
                clear_screen()
                self.ChucNang_bao_cao()
            elif lua_chon == "6":
                in_thong_tin("", "Đăng xuất thành công")
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
                        False,          # Tình trạng đăng nhập (mới tạo nên là True)
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
    def ChucNang_tim_kiem_khach_hang(self):
        in_thong_tin("MENU TÌM KIẾM KHÁCH HÀNG", "1. Tìm theo mã khách hàng\n2.Tìm theo tên khách hàng\n3. Tìm theo tên tài khoản\n4.Trở về Menu")
        try:
            lua_chon = STR_nhap_trong_khung("Nhập lựa chọn của bạn", "Nhập từ 1 đến 4")
            if lua_chon == "1":
                self.tim_theo_ma_khach_hang()
            elif lua_chon == "2":
                self.tim_theo_ten_khach_hang()
            elif lua_chon == "3":
                self.tim_theo_ten_tai_khoan()
            elif lua_chon == "4":
                clear_screen()
                self.ChucNang_menu()

            else:
                clear_screen()
                in_thong_tin_loi("Lựa chọn không hợp lệ", "Vui lòng thao tác lại")
                tiep_tuc()
                clear_screen()
                self.ChucNang_tim_kiem_khach_hang()
        except ValueError:
            in_thong_tin_loi("Lỗi", "Dừng chương trình")
            clear_screen()
            sys.exit()
    #Tìm kiếm khách hàng bằng mã khách hàng
    def tim_ma_kh(self, ma_khach_hang):
        for kh in self.khach_hang_list:
            if kh.lay_thong_tin("str_maKhachHang") == ma_khach_hang:
                return kh
        return None
    def tim_theo_ma_khach_hang(self):
       in_thong_tin("", "TÌM KIẾM THEO MÃ KHÁCH HÀNG")
       ma_khach_hang = STR_nhap_trong_khung ("Nhập mã khách hàng cần tìm: ", "")
       khach_hang = self.tim_ma_kh(ma_khach_hang)
       if khach_hang is None:
            in_thong_tin((f"Thông tin khách hàng có mã: {khach_hang.lay_thong_tin('str_maKhachHang')}", f"1. Họ tên: {khach_hang.lay_thong_tin('str_hoTen')}\n2. Mã khách hàng: {khach_hang.lay_thong_tin('str_maKhachHang')}\n3. Email: {khach_hang.lay_thong_tin('str_email')}\n4. Số điện thoại: {khach_hang.lay_thong_tin('int_soDienThoai')}\n5. Địa chỉ: {khach_hang.lay_thong_tin('str_diaChi')}\n6. Ngày sinh: {khach_hang.lay_thong_tin('date_ngaySinh')}\n7. Số tiền đã giao dịch: {khach_hang.lay_thong_tin('str_soTienDaGiaoDich')}\n8. Số lượng giao dịch: {khach_hang.lay_thong_tin('int_soLuongGiaoDich')}\n9. Điểm tích lũy: {khach_hang.lay_thong_tin('int_diemTichLuy')}\n10. Số tiền tiết kiệm: {khach_hang.lay_thong_tin('str_soTienTietKiem')}\n11. Hạng khách hàng: {khach_hang.lay_thong_tin('str_hangKhachHang')}"))
       else:
           in_thong_tin_loi("Không tìm thấy khách hàng với mã:", ma_khach_hang)
           try:
               ma_khach_hang = STR_nhap_trong_khung ("nhập lại mã khách hàng")
           except ValueError:
               in_thong_tin_loi("Không tìm thấy khách hàng với mã:", ma_khach_hang)
               tiep_tuc()
               clear_screen()
               self.ChucNang_tim_kiem_khach_hang()
    #Tìm kiếm khách hàng bằng tên khách hàng
    def tim_ten_kh(self, ho_ten):
        """ Tìm kiếm khách hàng theo tên khách."""
        for khach_hang in self.khach_hang_list:

            print(khach_hang)
            print("1\n")
            if khach_hang.lay_thong_tin('str_hoTen') == ho_ten:
               return khach_hang
        return None
    def tim_theo_ten_khach_hang(self):
       in_thong_tin("", "TÌM KIẾM THEO TÊN KHÁCH HÀNG")
       ho_ten = STR_nhap_trong_khung ("Nhập tên khách hàng cần tìm: ")
       khach_hang = self.tim_ten_kh(ho_ten)
       if khach_hang is None:
           in_thong_tin((f"Thông tin khách hàng có mã: {khach_hang.lay_thong_tin('str_maKhachHang')}", f"1. Họ tên: {khach_hang.lay_thong_tin('str_hoTen')}\n2. Mã khách hàng: {khach_hang.lay_thong_tin('str_maKhachHang')}\n3. Email: {khach_hang.lay_thong_tin('str_email')}\n4. Số điện thoại: {khach_hang.lay_thong_tin('int_soDienThoai')}\n5. Địa chỉ: {khach_hang.lay_thong_tin('str_diaChi')}\n6. Ngày sinh: {khach_hang.lay_thong_tin('date_ngaySinh')}\n7. Số tiền đã giao dịch: {khach_hang.lay_thong_tin('str_soTienDaGiaoDich')}\n8. Số lượng giao dịch: {khach_hang.lay_thong_tin('int_soLuongGiaoDich')}\n9. Điểm tích lũy: {khach_hang.lay_thong_tin('int_diemTichLuy')}\n10. Số tiền tiết kiệm: {khach_hang.lay_thong_tin('str_soTienTietKiem')}\n11. Hạng khách hàng: {khach_hang.lay_thong_tin('str_hangKhachHang')}"))
       else:
           in_thong_tin_loi("Không tìm thấy khách hàng với tên:", ho_ten)
           try:
               ho_ten = STR_nhap_trong_khung ("nhập lại tên khách hàng", "")
           except ValueError:
               in_thong_tin_loi("Không tìm thấy khách hàng với tên:", ho_ten)
               tiep_tuc()
               clear_screen()
               self.ChucNang_tim_kiem_khach_hang()
    #Tìm kiếm khách hàng bằng tên tài khoản
    def tim_ten_tk(self, ten_tai_khoan):
        """ Tìm kiếm khách hàng theo tên tài khoản."""
        for khach_hang in self.tai_khoan_list:
            if khach_hang.lay_thong_tin('str_tenTaiKhoan') == ten_tai_khoan: 
               return khach_hang
        return None
    def tim_theo_ten_tai_khoan(self):
       in_thong_tin("", "TÌM KIẾM THEO TÊN TÀI kHOẢN")
       ten_tai_khoan = STR_nhap_trong_khung ("Nhập tên tài khoản cần tìm: ")
       khach_hang = self.tim_ten_tk(ten_tai_khoan)
       if khach_hang is None:
           in_thong_tin((f"Thông tin khách hàng có mã: {khach_hang.lay_thong_tin('str_maKhachHang')}", f"1. Họ tên: {khach_hang.lay_thong_tin('str_hoTen')}\n2. Mã khách hàng: {khach_hang.lay_thong_tin('str_maKhachHang')}\n3. Email: {khach_hang.lay_thong_tin('str_email')}\n4. Số điện thoại: {khach_hang.lay_thong_tin('int_soDienThoai')}\n5. Địa chỉ: {khach_hang.lay_thong_tin('str_diaChi')}\n6. Ngày sinh: {khach_hang.lay_thong_tin('date_ngaySinh')}\n7. Số tiền đã giao dịch: {khach_hang.lay_thong_tin('str_soTienDaGiaoDich')}\n8. Số lượng giao dịch: {khach_hang.lay_thong_tin('int_soLuongGiaoDich')}\n9. Điểm tích lũy: {khach_hang.lay_thong_tin('int_diemTichLuy')}\n10. Số tiền tiết kiệm: {khach_hang.lay_thong_tin('str_soTienTietKiem')}\n11. Hạng khách hàng: {khach_hang.lay_thong_tin('str_hangKhachHang')}"))
       else:
           in_thong_tin_loi("Không tìm thấy khách hàng với tên tài khoản:", ten_tai_khoan)
           try:
               ho_ten = STR_nhap_trong_khung ("nhập lại tên tài khoản khách hàng")
           except ValueError:
               in_thong_tin_loi("Không tìm thấy khách hàng với tên:", ho_ten)
               tiep_tuc()
               clear_screen()
               self.ChucNang_tim_kiem_khach_hang()


# [3]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung
#xoakhachhang
    def ChucNang_xoa_khach_hang(self):
        in_thong_tin("MENU XÓA KHÁCH HÀNG", "1. Xóa khách hàng theo mã\n2. Trở về menu")

        try:
            lua_chon = STR_nhap_trong_khung("Nhập lựa chọn của bạn", "Nhập 1 hoặc 2")
            if lua_chon == "1":
                self.xoa_khach_hang()
                tiep_tuc()
                clear_screen()
                self.ChucNang_xoa_khach_hang()
            elif lua_chon == "2":
                in_thong_tin("THÔNG BÁO", "Quay lại menu chính.")
            else:
                in_thong_tin("LỖI", "Lựa chọn không hợp lệ. Vui lòng thao tác lại.")
                self.ChucNang_xoa_khach_hang()
        except ValueError:
            in_thong_tin("LỖI", "Dữ liệu nhập không hợp lệ. Vui lòng thao tác lại.")
            self.ChucNang_xoa_khach_hang()

    def xoa_khach_hang(self):
        in_thong_tin("CHỨC NĂNG XÓA KHÁCH HÀNG", "")
        ma_khach_hang = STR_nhap_trong_khung("Nhập mã khách hàng cần xóa", "Ví dụ: KH001")

        # Đọc danh sách khách hàng từ file
        danh_sach_khach_hang = self.doc_du_lieu_tu_file('Database/khach_hang.csv', 'khach_hang')

        # Tìm kiếm khách hàng theo mã
        khach_hang = next((kh for kh in danh_sach_khach_hang if kh.lay_thong_tin("str_maKhachHang") == ma_khach_hang), None)
        if not khach_hang:
            in_thong_tin("THÔNG BÁO", "Khách hàng không tồn tại. Vui lòng kiểm tra lại mã khách hàng.")
            return

        # Hiển thị thông tin khách hàng
        thong_tin = "\n".join(f"{key}: {value}" for key, value in khach_hang.items())
        in_thong_tin("THÔNG TIN KHÁCH HÀNG", thong_tin)

        # Xác nhận thao tác
        xac_nhan = STR_nhap_trong_khung("Bạn có chắc chắn muốn xóa khách hàng này?", "co/khong").lower()
        if xac_nhan != 'co':
            in_thong_tin("THÔNG BÁO", "Hủy thao tác xóa khách hàng.")
            return

        # Xóa khách hàng khỏi danh sách
        danh_sach_khach_hang.remove(khach_hang)

        # Lưu danh sách cập nhật lại file
        self.luu_du_lieu(danh_sach_khach_hang)

        # Thông báo thành công
        in_thong_tin("THÀNH CÔNG", "Khách hàng đã được xóa thành công.")

    # def doc_du_lieu(self):
    #     """Đọc dữ liệu khách hàng từ file CSV."""
    #     try:
    #         with open('khach_hang.csv', 'r', encoding='utf-8') as file:
    #             reader = csv.DictReader(file)
    #             return list(reader)
    #     except FileNotFoundError:
    #         return []

    def luu_du_lieu(self, danh_sach_khach_hang):
        """Lưu danh sách khách hàng vào file CSV."""
        with open('khach_hang.csv', 'w', encoding='utf-8', newline='') as file:
            if danh_sach_khach_hang:
                fieldnames = danh_sach_khach_hang[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(danh_sach_khach_hang)

# [4]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung

    def ChucNang_chinh_sua_khach_hang(self):
        in_thong_tin("CHỈNH SỬA THÔNG TIN KHÁCH HÀNG", "1. Chỉnh sửa thông tin khách hàng\n2. Trở về menu")
        lua_chon = STR_nhap_trong_khung("Nhập lựa chọn của bạn", "Nhập 1 hoặc 2")
        if lua_chon == "1":
            self.chinh_sua_khach_hang()
            tiep_tuc()
            clear_screen()
        elif lua_chon == "2":
            self.ChucNang_menu()
            tiep_tuc()
            clear_screen()
        else:
            in_thong_tin_loi("Lựa chọn không hợp lệ", "Vui lòng thao tác lại")
            tiep_tuc()
            clear_screen()
            self.ChucNang_chinh_sua_khach_hang()
        
    def chinh_sua_khach_hang(self):
        in_thong_tin("", "CHỈNH SỬA THÔNG TIN KHÁCH HÀNG")
        ma_khach_hang = STR_nhap_trong_khung("Nhập mã khách hàng cần chỉnh sửa", "Mã khách hàng")
        khach_hang = self.tim_khach_hang(ma_khach_hang)
        tiep_tuc()
        clear_screen()
        if khach_hang is None:
            in_thong_tin_loi("Không tìm thấy khách hàng", "Vui lòng nhập lại mã khách hàng")
            tiep_tuc()
            clear_screen()
            self.chinh_sua_khach_hang()
        while True:
            in_thong_tin(f"Thông tin khách hàng có mã: {khach_hang.lay_thong_tin('str_maKhachHang')}", f"1. Họ tên: {khach_hang.lay_thong_tin('str_hoTen')}\n2. Mã khách hàng: {khach_hang.lay_thong_tin('str_maKhachHang')}\n3. Email: {khach_hang.lay_thong_tin('str_email')}\n4. Số điện thoại: {khach_hang.lay_thong_tin('int_soDienThoai')}\n5. Địa chỉ: {khach_hang.lay_thong_tin('str_diaChi')}\n6. Ngày sinh: {khach_hang.lay_thong_tin('date_ngaySinh')}\n7. Số tiền đã giao dịch: {khach_hang.lay_thong_tin('str_soTienDaGiaoDich')}\n8. Số lượng giao dịch: {khach_hang.lay_thong_tin('int_soLuongGiaoDich')}\n9. Điểm tích lũy: {khach_hang.lay_thong_tin('int_diemTichLuy')}\n10. Số tiền tiết kiệm: {khach_hang.lay_thong_tin('str_soTienTietKiem')}\n11. Hạng khách hàng: {khach_hang.lay_thong_tin('str_hangKhachHang')}\n12. Đổi mật khẩu cho khách hàng")
            try:
                lua_chon = int(STR_nhap_trong_khung("Nhập số để chỉnh sửa thông tin", "Nhập (1-12), 13 để về Menu"))
            except ValueError:
                in_thong_tin_loi("Lỗi", "Vui lòng nhập số hợp lệ")
                continue
            # Chỉnh sửa thông tin khách hàng theo các số
            if lua_chon == 1:
                str_hoTen = STR_nhap_trong_khung("Nhập họ tên mới", khach_hang.lay_thong_tin("str_hoTen"))
                if str_hoTen:
                    str_hoTen = str_hoTen.title()
                    khach_hang.chinh_thong_tin("str_hoTen", str_hoTen)
                    in_thong_tin("Thông báo", "Cập nhật họ tên thành công")
                    self.luu_du_lieu_vao_file()
                else:
                    in_thong_tin_loi("Lỗi", "Họ tên không được để trống.")
            elif lua_chon == 2:
                in_thong_tin_loi("Thông báo", "Mã khách hàng không thể chỉnh sửa, chọn lại lựa chọn khác")

            elif lua_chon == 3:
                str_email = STR_nhap_trong_khung("Nhập email mới", khach_hang.lay_thong_tin("str_email"))
                while not BOOL_kiem_tra_email(str_email):
                    in_thong_tin_loi("Lỗi", "Email không hợp lệ. Vui lòng nhập lại.")
                    str_email = STR_nhap_trong_khung("Nhập Email", "Email liên hệ")
                # Kiểm tra email không trùng
                if self.kiem_tra_email_trung(str_email):
                    in_thong_tin_loi("Lỗi", "Email đã tồn tại. Vui lòng nhập email khác.")
                    continue
                khach_hang.chinh_thong_tin("str_email", str_email)
                in_thong_tin("Thông báo", "Cập nhật email thành công")
                self.luu_du_lieu_vao_file()
            elif lua_chon == 4:
                int_soDienThoai = STR_nhap_trong_khung("Nhập số điện thoại mới", khach_hang.lay_thong_tin("int_soDienThoai"))
                while not BOOL_kiem_tra_so_dien_thoai(int_soDienThoai):
                    in_thong_tin_loi("Lỗi", "Số điện thoại không hợp lệ. Vui lòng nhập lại.")
                    int_soDienThoai = STR_nhap_trong_khung("Nhập số điện thoại", "Nhập số")
                # Kiểm tra số điện thoại không trùng
                if self.kiem_tra_so_dien_thoai_trung(int_soDienThoai):
                    in_thong_tin_loi("Lỗi", "Số điện thoại đã tồn tại. Vui lòng nhập số khác.")
                    continue
                khach_hang.chinh_thong_tin("int_soDienThoai", int_soDienThoai)
                in_thong_tin("Thông báo", "Cập nhật số điện thoại thành công")
                self.luu_du_lieu_vao_file()
            elif lua_chon == 5:
                str_diaChi = STR_nhap_trong_khung("Nhập địa chỉ mới", khach_hang.lay_thong_tin("str_diaChi"))
                if str_diaChi:
                    str_diaChi = str_diaChi.title()
                    khach_hang.chinh_thong_tin("str_diaChi", str_diaChi)
                    in_thong_tin("Thông báo", "Cập nhật địa chỉ thành công")
                    self.luu_du_lieu_vao_file()
                else:
                    in_thong_tin_loi("Lỗi", "Địa chỉ không được để trống.")
            elif lua_chon == 6:
                date_ngaySinh = STR_nhap_trong_khung("Nhập ngày sinh (YYYY-MM-DD)", khach_hang.lay_thong_tin("date_ngaySinh"))
                if BOOL_kiem_tra_ngay_sinh(date_ngaySinh):
                    khach_hang.chinh_thong_tin("date_ngaySinh", date_ngaySinh)
                    in_thong_tin("Thông báo", "Cập nhật ngày sinh thành công")
                    self.luu_du_lieu_vao_file()
                else:
                    in_thong_tin_loi("Lỗi", "Ngày sinh không hợp lệ. Vui lòng nhập lại.")
            elif lua_chon == 7:
                str_soTienDaGiaoDich = STR_nhap_trong_khung("Nhập số tiền đã giao dịch mới", str(khach_hang.lay_thong_tin("str_soTienDaGiaoDich")))
                khach_hang.chinh_thong_tin("str_soTienDaGiaoDich", str_soTienDaGiaoDich)
                khach_hang.tinh_diem_tich_luy()
                khach_hang.phan_loai_khach_hang()
                in_thong_tin("Thông báo", "Cập nhật số tiền giao dịch thành công")
                self.luu_du_lieu_vao_file()
            elif lua_chon == 8:
                int_soLuongGiaoDich = int(STR_nhap_trong_khung("Nhập số lượng giao dịch mới", str(khach_hang.lay_thong_tin("int_soLuongGiaoDich"))))
                khach_hang.chinh_thong_tin("int_soLuongGiaoDich", int_soLuongGiaoDich)
                in_thong_tin("Thông báo", "Cập nhật số lượng giao dịch thành công")
                self.luu_du_lieu_vao_file()
            elif lua_chon == 9:  
                int_diemTichLuy = int(STR_nhap_trong_khung("Nhập điểm tích lũy mới", str(khach_hang.lay_thong_tin("int_diemTichLuy"))))
                khach_hang.chinh_thong_tin("int_diemTichLuy", int_diemTichLuy)
                # Tự động phân loại lại hạng khách hàng sau khi cập nhật điểm tích lũy
                khach_hang.phan_loai_khach_hang()
                in_thong_tin("Thông báo", "Cập nhật điểm tích lũy và hạng khách hàng đã được tự động cập nhật")
                self.luu_du_lieu_vao_file()
            elif lua_chon == 10:
                str_soTienTietKiem = STR_nhap_trong_khung("Nhập số tiền tiết kiệm mới", khach_hang.lay_thong_tin("str_soTienTietKiem"))
                khach_hang.chinh_thong_tin("str_soTienTietKiem", str_soTienTietKiem)
                in_thong_tin("Thông báo", "Cập nhật số tiền tiết kiệm thành công")
                self.luu_du_lieu_vao_file()
            elif lua_chon == 11:
                in_thong_tin_loi("Thông báo", "Không thể chỉnh sửa hạng khách hàng, hạng khách hàng được tự động cập nhật")
            elif lua_chon == 12:
                mat_khau = STR_nhap_trong_khung("Nhập mật khẩu mới", "")
                for tk in self.tai_khoan_list:
                    if tk.lay_thong_tin("str_maNguoiDung")== ma_khach_hang:
                        tk.chinhSuaThongTin(mat_khau=mat_khau)
                        in_thong_tin("Thông báo", "Cập nhật mật khẩu thành công")
                        self.luu_du_lieu_vao_file()
                        break
            elif lua_chon == 13:
                in_thong_tin_loi("Thông báo", "Về Menu chương trình")
                tiep_tuc()
                clear_screen()
                self.ChucNang_menu()
            lua_chon_tiep = STR_nhap_trong_khung("Bạn có muốn sửa thêm thông tin không? (c: Có / k: Không)", "Nhập c để tiếp tục, k để thoát")
            if lua_chon_tiep.lower() == 'k':
                in_thong_tin("Thông báo", "Thoát chức năng chỉnh sửa thông tin khách hàng")
                self.ChucNang_menu()
                break
            tiep_tuc()
            clear_screen()
                
    def tim_khach_hang(self, ma_khach_hang):
        for kh in self.khach_hang_list:
            if kh.lay_thong_tin("str_maKhachHang") == ma_khach_hang:
                return kh
        return None
    
    def kiem_tra_so_dien_thoai_trung(self, so_dien_thoai):
        # Kiểm tra số điện thoại trong danh sách khách hàng
        for kh in self.khach_hang_list:
            if kh.lay_thong_tin('int_soDienThoai') == so_dien_thoai:
                return True  # Số điện thoại đã tồn tại
        return False  # Số điện thoại không trùng

    def kiem_tra_email_trung(self, email):
        # Kiểm tra email trong danh sách khách hàng
        for kh in self.khach_hang_list:
            if kh.lay_thong_tin('str_email') == email:
                return True  # Email đã tồn tại
        return False  # Email không trùng
# [5]
# Viết tất cả các hàm chức năng dưới này kèm comment
# In ra nhớ dùng in_thong_tin và lấy ký tự nhớ dùng STR_nhap_trong_khung
    # def ChucNang_dang_nhap(self):
    #     """
    #     Hàm chức năng đăng nhập
    #     - Yêu cầu nhập tên đăng nhập và mật khẩu
    #     - Xác thực thông tin người dùng
    #     """
    #     in_thong_tin("ĐĂNG NHẬP HỆ THỐNG", "Vui lòng nhập thông tin đăng nhập")
        
    #     # Nhập tên đăng nhập
    #     ten_dang_nhap = STR_nhap_trong_khung("Nhập tên đăng nhập", "Tên đăng nhập")
        
    #     # Nhập mật khẩu
    #     mat_khau = STR_nhap_trong_khung("Nhập mật khẩu", "Mật khẩu")
        
    #     # Kiểm tra tên đăng nhập và mật khẩu
    #     if self.kiem_tra_dang_nhap(ten_dang_nhap, mat_khau):
    #         in_thong_tin("Thông báo", "Đăng nhập thành công!")
    #         self.ChucNang_menu()  # Sau khi đăng nhập thành công, chuyển đến menu chính
    #     else:
    #         in_thong_tin_loi("Lỗi", "Tên đăng nhập hoặc mật khẩu không chính xác")
    #         tiep_tuc()
    #         clear_screen()
    #         self.ChucNang_dang_nhap()  # Nếu sai, yêu cầu nhập lại thông tin

    # def kiem_tra_dang_nhap(self, ten_dang_nhap, mat_khau):
    #     """
    #     Kiểm tra tên đăng nhập và mật khẩu có hợp lệ hay không
    #     - So sánh với dữ liệu đã lưu trữ (ví dụ: trong một danh sách người dùng hoặc file)
    #     """
    #     # Ví dụ kiểm tra danh sách người dùng, cần thay đổi theo cách bạn lưu trữ dữ liệu
    #     for user in self.danh_sach_nguoi_dung:
    #         if user.ten_dang_nhap == ten_dang_nhap and user.mat_khau == mat_khau:
    #             return True
    #     return False


    # def ChucNang_bao_cao(self):
    #     """
    #     Hàm chức năng báo cáo
    #     - Hiển thị các thống kê báo cáo về khách hàng
    #     """
    #     in_thong_tin("BÁO CÁO HỆ THỐNG", "1. Báo cáo danh sách khách hàng\n2. Báo cáo số lượng khách hàng mới\n3. Báo cáo phân loại khách hàng\n4. Báo cáo giao dịch khách hàng\n5. Trở về menu")

    #     lua_chon = STR_nhap_trong_khung("Nhập lựa chọn báo cáo", "Nhập 1, 2, 3, 4 hoặc 5 để chọn")

    #     if lua_chon == "1":
    #         self.bao_cao_danh_sach_khach_hang()
    #     elif lua_chon == "2":
    #         self.bao_cao_so_luong_khach_hang_moi()
    #     elif lua_chon == "3":
    #         self.bao_cao_phan_loai_khach_hang()
    #     elif lua_chon == "4":
    #         self.bao_cao_giao_dich_khach_hang()
    #     elif lua_chon == "5":
    #         self.ChucNang_menu()  # Trở về menu chính
    #     else:
    #         in_thong_tin_loi("Lỗi", "Lựa chọn không hợp lệ, vui lòng nhập lại")
    #         tiep_tuc()
    #         clear_screen()
    #         self.ChucNang_bao_cao()
    
    # def bao_cao_danh_sach_khach_hang(self):
    #     """
    #     Báo cáo danh sách tất cả khách hàng
    #     - Hiển thị thông tin đầy đủ của tất cả khách hàng trong hệ thống
    #     """
    #     in_thong_tin("BÁO CÁO DANH SÁCH KHÁCH HÀNG", "Danh sách tất cả khách hàng trong hệ thống:")

    #     # Duyệt qua từng khách hàng và in thông tin
    #     for kh in self.khach_hang_list:
    #         in_thong_tin("", f"Khách hàng: {kh.lay_thong_tin('str_hoTen')}\nNgày sinh: {kh.lay_thong_tin('date_ngaySinh')}\nHạng: {kh.lay_thong_tin('str_hangKhachHang')}")
        
    #     tiep_tuc()  # Đợi người dùng nhấn tiếp tục
    #     clear_screen()  # Dọn dẹp màn hình
    #     self.ChucNang_bao_cao()  # Quay lại menu báo cáo
    
    # def bao_cao_so_luong_khach_hang_moi(self):
    #     """
    #     Báo cáo số lượng khách hàng mới
    #     - Hiển thị số lượng khách hàng mới trong một khoảng thời gian do người dùng nhập vào
    #     """
    #     in_thong_tin("BÁO CÁO SỐ LƯỢNG KHÁCH HÀNG MỚI", "Nhập khoảng thời gian cần báo cáo (Ví dụ: YYYY-MM-DD - YYYY-MM-DD)")
        
    #     # Nhập khoảng thời gian
    #     start_date = STR_nhap_trong_khung("Nhập ngày bắt đầu (YYYY-MM-DD)", "Ngày bắt đầu")
    #     end_date = STR_nhap_trong_khung("Nhập ngày kết thúc (YYYY-MM-DD)", "Ngày kết thúc")
        
    #     # Lọc khách hàng mới trong khoảng thời gian
    #     khach_hang_moi = [kh for kh in self.khach_hang_list if start_date <= kh.lay_thong_tin('date_ngaySinh') <= end_date]
        
    #     # In thông tin báo cáo
    #     in_thong_tin("BÁO CÁO SỐ LƯỢNG KHÁCH HÀNG MỚI", f"Số lượng khách hàng mới trong khoảng thời gian {start_date} - {end_date}: {len(khach_hang_moi)}")
        
    #     # Hiển thị thông tin chi tiết
    #     for kh in khach_hang_moi:
    #         in_thong_tin("", f"Khách hàng: {kh.lay_thong_tin('str_hoTen')}\nNgày đăng ký: {kh.lay_thong_tin('date_ngaySinh')}")
        
    #     tiep_tuc()  # Đợi người dùng nhấn tiếp tục
    #     clear_screen()  # Dọn dẹp màn hình
    #     self.ChucNang_bao_cao()  # Quay lại menu báo cáo
    
    # def bao_cao_phan_loai_khach_hang(self):
    #     """
    #     Báo cáo phân loại khách hàng
    #     - Hiển thị khách hàng theo từng nhóm hạng: VIP, thường xuyên, mới
    #     """
    #     # Phân loại khách hàng theo hạng
    #     khach_hang_vip = [kh for kh in self.khach_hang_list if kh.lay_thong_tin('str_hangKhachHang') == "VIP"]
    #     khach_hang_thuong_xuyen = [kh for kh in self.khach_hang_list if kh.lay_thong_tin('str_hangKhachHang') == "Thường xuyên"]
    #     khach_hang_moi = [kh for kh in self.khach_hang_list if kh.lay_thong_tin('str_hangKhachHang') == "Mới"]
        
    #     # In thông tin báo cáo
    #     in_thong_tin("BÁO CÁO PHÂN LOẠI KHÁCH HÀNG", "Danh sách khách hàng theo từng hạng:")
        
    #     in_thong_tin("", f"VIP ({len(khach_hang_vip)} khách hàng):")
    #     for kh in khach_hang_vip:
    #         in_thong_tin("", f"Khách hàng: {kh.lay_thong_tin('str_hoTen')}\nHạng: {kh.lay_thong_tin('str_hangKhachHang')}")
        
    #     in_thong_tin("", f"Thường xuyên ({len(khach_hang_thuong_xuyen)} khách hàng):")
    #     for kh in khach_hang_thuong_xuyen:
    #         in_thong_tin("", f"Khách hàng: {kh.lay_thong_tin('str_hoTen')}\nHạng: {kh.lay_thong_tin('str_hangKhachHang')}")
        
    #     in_thong_tin("", f"Mới ({len(khach_hang_moi)} khách hàng):")
    #     for kh in khach_hang_moi:
    #         in_thong_tin("", f"Khách hàng: {kh.lay_thong_tin('str_hoTen')}\nHạng: {kh.lay_thong_tin('str_hangKhachHang')}")
        
    #     tiep_tuc()  # Đợi người dùng nhấn tiếp tục
    #     clear_screen()  # Dọn dẹp màn hình
    #     self.ChucNang_bao_cao()  # Quay lại menu báo cáo
    
    # def bao_cao_giao_dich_khach_hang(self):
    #     """
    #     Báo cáo giao dịch khách hàng
    #     - Liệt kê giao dịch của khách hàng, bao gồm số tiền và ngày giao dịch
    #     """
    #     # In tiêu đề báo cáo
    #     in_thong_tin("BÁO CÁO GIAO DỊCH KHÁCH HÀNG", "Danh sách giao dịch của khách hàng:")
        
    #     # Duyệt qua từng khách hàng và in giao dịch
    #     for kh in self.khach_hang_list:
    #         giao_dich_list = kh.lay_thong_tin('list_giaoDich')
            
    #         if giao_dich_list:
    #             for gd in giao_dich_list:
    #                 in_thong_tin("", f"Khách hàng: {kh.lay_thong_tin('str_hoTen')}\nGiao dịch: {gd['soTien']} VND vào ngày {gd['ngayGiaoDich']}")
    #         else:
    #             in_thong_tin("", f"Khách hàng {kh.lay_thong_tin('str_hoTen')} không có giao dịch nào.")
        
    #     tiep_tuc()  # Đợi người dùng nhấn tiếp tục
    #     clear_screen()  # Dọn dẹp màn hình
    #     self.ChucNang_bao_cao()  # Quay lại menu báo cáo