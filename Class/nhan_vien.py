from Class.nguoi import Nguoi

class NhanVien(Nguoi):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, ma_nhan_vien, chuc_vu, phong_ban):
        """
        Khởi tạo đối tượng NhanVien, kế thừa từ Nguoi.
        """
        super().__init__(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email)
        self.__str_maNhanVien = str(ma_nhan_vien)  
        self.__str_chucVu = str(chuc_vu)  
        self.__str_phongBan = str(phong_ban) 

    def __str__(self):
        return (f"NhanVien[MaNV={self.__str_maNhanVien}, ChucVu={self.__str_chucVu}, PhongBan={self.__str_phongBan}, "
                f"LuongCoBan={self.__luong_co_ban}, {super().__str__()}]")
    def hien_thi_thong_tin(self):
        print(self)
    def lay_thong_tin(self, attr_name):
        """Lấy thông tin của tài khoản dựa trên tên thuộc tính."""
        # Tìm thuộc tính trong lớp hiện tại
        attr_value = getattr(self, f"_{self.__class__.__name__}__{attr_name}", None)
        if attr_value is not None:
            return attr_value
        # Nếu không tìm thấy, tiếp tục tìm trong lớp cha Nguoi
        return getattr(self, f"_{Nguoi.__name__}__{attr_name}", None)
    