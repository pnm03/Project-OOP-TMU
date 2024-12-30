from Class.nguoi import Nguoi

class KhachHang(Nguoi):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, 
                 ma_khach_hang, hang_khach_hang, so_tien_da_giao_dich, 
                 so_luong_giao_dich, ngay_tao_tai_khoan, diem_tich_luy, so_tien_tiet_kiem):
        """
        Khởi tạo đối tượng KhachHang, kế thừa từ lớp Nguoi.
        """
        super().__init__(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email)
        self.__str_maKhachHang = str(ma_khach_hang)  
        self.__str_hangKhachHang = str(hang_khach_hang)
        self.__str_soTienDaGiaoDich = str(so_tien_da_giao_dich) 
        self.__int_soLuongGiaoDich = int(so_luong_giao_dich)
        self.__date_ngayTaoTaiKhoan = ngay_tao_tai_khoan  
        self.__int_diemTichLuy = int(diem_tich_luy)
        self.__str_soTienTietKiem = str(so_tien_tiet_kiem) 
        self.tinh_diem_tich_luy()
        self.phan_loai_khach_hang()

    def __str__(self):
        return (f"KhachHang[MaKH={self.__str_maKhachHang}, HangKH={self.__str_hangKhachHang}, "
                f"SoTienGD={self.__str_soTienDaGiaoDich}, SoLuongGD={self.__int_soLuongGiaoDich}, "
                f"NgayTaoTK={self.__date_ngayTaoTaiKhoan}, DiemTichLuy={self.__int_diemTichLuy}, "
                f"SoTienTietKiem={self.__str_soTienTietKiem}, {super().__str__()}]")


    def hien_thi_thong_tin(self):
        print(self)

    def lay_thong_tin(self, attr_name):
        """Lấy thông tin của khách hàng dựa trên tên thuộc tính."""
        # Kiểm tra thuộc tính có trong lớp KhachHang
        kh_attr = getattr(self, f"_{self.__class__.__name__}__{attr_name}", None)
        if kh_attr is not None:
            return kh_attr
        # Nếu không tìm thấy, kiểm tra thuộc tính trong lớp Nguoi
        return getattr(self, f"_{Nguoi.__name__}__{attr_name}", None)

    def chinh_thong_tin(self, attr_name, value):
        if attr_name == "str_maKhachHang":
            print(f"Không thể chỉnh sửa thuộc tính {attr_name}.")
            return

        # Kiểm tra thuộc tính có trong lớp KhachHang
        if hasattr(self, f"_{self.__class__.__name__}__{attr_name}"):
            setattr(self, f"_{self.__class__.__name__}__{attr_name}", value)
        # Nếu không tìm thấy ở lớp KhachHang, kiểm tra ở lớp Nguoi
        elif hasattr(self, f"_{Nguoi.__name__}__{attr_name}"):
            setattr(self, f"_{Nguoi.__name__}__{attr_name}", value)
        else:
            print(f"Thuộc tính {attr_name} không tồn tại.")



    def tinh_diem_tich_luy(self):
        self.__int_diemTichLuy = int(float(self.__str_soTienDaGiaoDich) * 0.01)

    def phan_loai_khach_hang(self):
        if self.__int_diemTichLuy >= 800000:
            self.__str_hangKhachHang = "VIP"
        elif self.__int_diemTichLuy >= 200000:
            self.__str_hangKhachHang = "Thân thiết"
        else:
            self.__str_hangKhachHang = "Thường"