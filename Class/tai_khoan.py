
from Config.function import *
class TaiKhoan:
    def __init__(self, ten_tai_khoan, mat_khau, ma_nguoi_dung, tinh_trang_dang_nhap, so_lan_da_dang_nhap):
        self.__str_tenTaiKhoan = str(ten_tai_khoan)
        self.__str_matKhau = str(mat_khau)
        self.__str_maNguoiDung = str(ma_nguoi_dung)
        self.__bool_tinhTrangDangNhap = tinh_trang_dang_nhap
        self.__int_soLanDaDangNhap = int(so_lan_da_dang_nhap)

    

    def Bool_kiemTraMatKhau(self, ten_tai_khoan, mat_khau):
        """Kiểm tra tài khoản và mật khẩu."""
        if self.__str_tenTaiKhoan == ten_tai_khoan:
            if self.__str_matKhau == mat_khau:
                self.__bool_tinhTrangDangNhap = True
                self.__int_soLanDaDangNhap = 0  # Reset số lần đăng nhập sai
                return True
            else:
                # Nếu mật khẩu sai, tăng số lần đăng nhập sai
                if "KH" in self.__str_maNguoiDung:
                    self.__int_soLanDaDangNhap += 1
                return False
        return False  # Tên tài khoản không khớp



    def hien_thi_thong_tin(self):
        """Hiển thị thông tin tài khoản."""
        in_thong_tin("Thông Tin Tài Khoản", f"Tài Khoản: {self.__str_tenTaiKhoan}\nMã Người Dùng: {self.__str_maNguoiDung}\nTình Trạng: {'Active' if self.__bool_tinhTrangDangNhap else 'Locked'}\nSố Lần Đăng Nhập Sai: {self.__int_soLanDaDangNhap}")

    def lay_thong_tin(self, attr_name):
        """Lấy thông tin thuộc tính theo tên."""
        return getattr(self, f"_{self.__class__.__name__}__{attr_name}", None)

    def chinhSuaThongTin(self, ten_tai_khoan=None, mat_khau=None, tinh_trang_dang_nhap=None, so_lan_da_dang_nhap=None):
        """Chỉnh sửa thông tin của tài khoản, không thể chỉnh sửa mã người dùng."""
        if ten_tai_khoan is not None:
            self.__str_tenTaiKhoan = ten_tai_khoan
        if mat_khau is not None:
            
            self.__str_matKhau = mat_khau
            print(f"Mật khẩu đã được thay đổi thành công!")
        if tinh_trang_dang_nhap is not None:
            self.__bool_tinhTrangDangNhap = tinh_trang_dang_nhap
        if so_lan_da_dang_nhap is not None:
            self.__int_soLanDaDangNhap = so_lan_da_dang_nhap