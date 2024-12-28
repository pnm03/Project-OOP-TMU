from Class.nguoi import Nguoi

class NhanVien(Nguoi):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, ma_nhan_vien, chuc_vu, phong_ban):
        """
        Khởi tạo đối tượng NhanVien, kế thừa từ Nguoi.
        """
        super().__init__(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email)
        self.str_maNhanVien = str(ma_nhan_vien)  
        self.str_chucVu = str(chuc_vu)  
        self.str_phongBan = str(phong_ban) 

    def __str__(self):
        return (f"NhanVien[MaNV={self.str_maNhanVien}, ChucVu={self.str_chucVu}, PhongBan={self.str_phongBan}, "
                f"LuongCoBan={self.luong_co_ban}, {super().__str__()}]")