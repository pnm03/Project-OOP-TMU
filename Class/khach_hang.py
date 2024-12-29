from Class.nguoi import Nguoi

class KhachHang(Nguoi):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, 
                 ma_khach_hang, hang_khach_hang, so_tien_da_giao_dich, 
                 so_luong_giao_dich, ngay_tao_tai_khoan, diem_tich_luy, so_tien_tiet_kiem):
        """
        Khởi tạo đối tượng KhachHang, kế thừa từ lớp Nguoi.
        """
        super().__init__(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email)
        self.str_maKhachHang = str(ma_khach_hang)  
        self.bool_hangKhachHang = hang_khach_hang
        self.str_soTienDaGiaoDich = str(so_tien_da_giao_dich) 
        self.int_soLuongGiaoDich = int(so_luong_giao_dich)
        self.date_ngayTaoTaiKhoan = ngay_tao_tai_khoan  
        self.int_diemTichLuy = int(diem_tich_luy)
        self.str_soTienTietKiem = str(so_tien_tiet_kiem) 

    # Các phương thức khác...

    def __str__(self):
        return (f"KhachHang[MaKH={self.str_maKhachHang}, HangKH={self.bool_hangKhachHang}, "
                f"SoTienGD={self.str_soTienDaGiaoDich}, SoLuongGD={self.int_soLuongGiaoDich}, "
                f"NgayTaoTK={self.date_ngayTaoTaiKhoan}, DiemTichLuy={self.int_diemTichLuy}, "
                f"SoTienTietKiem={self.str_soTienTietKiem}, {super().__str__()}]")
    