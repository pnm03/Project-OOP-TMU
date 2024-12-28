class TaiKhoan:
    def __init__(self, ten_tai_khoan, mat_khau, ma_nguoi_dung, tinh_trang_dang_nhap, so_lan_da_dang_nhap):
        """
        Khởi tạo đối tượng TaiKhoan từ các tham số.
        """
        self.str_tenTaiKhoan = str(ten_tai_khoan) 
        self.str_matKhau = str(mat_khau) 
        self.str_maNguoiDung = str(ma_nguoi_dung) 
        self.bool_tinhTrangDangNhap = tinh_trang_dang_nhap
        self.int_soLanDaDangNhap = int(so_lan_da_dang_nhap) 

    def __str__(self):
        return (f"TaiKhoan[TenTK={self.str_tenTaiKhoan}, MaNguoiDung={self.str_maNguoiDung}, "
                f"TinhTrangDangNhap={self.bool_tinhTrangDangNhap}, SoLanDangNhap={self.int_soLanDaDangNhap}]")
