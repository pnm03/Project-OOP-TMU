from Config.function import *
class TaiKhoan:
    def __init__(self, ten_tai_khoan, mat_khau, ma_nguoi_dung, tinh_trang_dang_nhap, so_lan_da_dang_nhap):
        """
        Khởi tạo đối tượng TaiKhoan từ các tham số.
        """
        self.__str_tenTaiKhoan = str(ten_tai_khoan) 
        self.__str_matKhau = str(mat_khau) 
        self.__str_maNguoiDung = str(ma_nguoi_dung) 
        self.__bool_tinhTrangDangNhap = tinh_trang_dang_nhap
        self.__int_soLanDaDangNhap = int(so_lan_da_dang_nhap) 

    def __str__(self):
        return (f"TaiKhoan[TenTK={self.__str_tenTaiKhoan}, MaNguoiDung={self.__str_maNguoiDung}, "
                f"TinhTrangDangNhap={self.__bool_tinhTrangDangNhap}, SoLanDangNhap={self.__int_soLanDaDangNhap}]")
    def Bool_kiemTraMatKhau(self, ten_tai_khoan, mat_khau):
        # Kiểm tra nếu tài khoản đã bị khóa
        if self.__int_soLanDaDangNhap > 3:
            in_thong_tin_loi("Tài khoản bị khóa", "Tài khoản đã bị khóa do nhập sai mật khẩu quá 3 lần. Vui lòng liên hệ quản trị viên để mở khóa hoặc xin cấp lại mật khẩu")
            return False
        
        if ten_tai_khoan == self.__str_tenTaiKhoan:
            if mat_khau == self.__str_matKhau:
                # Mật khẩu đúng, gán trạng thái đăng nhập là 1 và số lần đăng nhập là 0
                self.__bool_tinhTrangDangNhap = 1
                self.__int_soLanDaDangNhap = 0
                return True
            else:
                # Mật khẩu sai, tăng số lần đăng nhập lên 1
                self.__int_soLanDaDangNhap += 1
                if self.__int_soLanDaDangNhap > 3:
                    in_thong_tin_loi("Cảnh báo", "Tài khoản bị khóa do nhập sai mật khẩu quá 3 lần!")
                    print("Tài khoản bị khóa do nhập sai mật khẩu quá 3 lần!")
                    return False
                else:
                    in_thong_tin_loi("", "Sai tài khoản hoặc mật khẩu!")
                    return False
        else:
            in_thong_tin_loi("", "Sai tài khoản hoặc mật khẩu!")
            return False
    
    def hien_thi_thong_tin(self):
        print(self)
    
    def lay_thong_tin(self, attr_name):
        """Lấy thông tin của tài khoản dựa trên tên thuộc tính."""
        # Nếu mã người dùng có chứa "NV", không cho lấy mật khẩu
        if attr_name == "str_matKhau" and "NV" in self.__str_maNguoiDung:
            print("Không thể xem mật khẩu của nhân viên!")
            return None
        # Lấy giá trị thuộc tính
        return getattr(self, f"_{self.__class__.__name__}__{attr_name}", None)
    def chinhSuaThongTin(self, ten_tai_khoan=None, mat_khau=None, tinh_trang_dang_nhap=None, so_lan_da_dang_nhap=None):
        """Chỉnh sửa thông tin của tài khoản, không thể chỉnh sửa mã người dùng."""
        if ten_tai_khoan is not None:
            self.__str_tenTaiKhoan = ten_tai_khoan
        if mat_khau is not None:
            if "KH" in self.__str_maNguoiDung:
                self.__str_matKhau = mat_khau
                print(f"Mật khẩu đã được thay đổi thành công!")
            else:
                print("Chỉ thay đổi được mật khẩu của khách hàng")
        if tinh_trang_dang_nhap is not None:
            self.__bool_tinhTrangDangNhap = tinh_trang_dang_nhap
        if so_lan_da_dang_nhap is not None:
            self.__int_soLanDaDangNhap = so_lan_da_dang_nhap
