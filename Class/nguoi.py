class Nguoi:
    def __init__(self, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email):
        """
        Khởi tạo đối tượng Nguoi từ các tham số.
        """
        self.__str_hoTen = ho_ten
        self.__date_ngaySinh = ngay_sinh  
        self.__str_diaChi = dia_chi
        self.__int_soDienThoai = so_dien_thoai
        self.__str_email = email

    def __str__(self):
        return (f"Nguoi[HoTen={self.__str_hoTen}, NgaySinh={self.__date_ngaySinh}, "
            f"DiaChi={self.__str_diaChi}, SoDienThoai={self.__int_soDienThoai}, Email={self.__str_email}]")
    def hienThiThongTin(self):
        pass
    def lay_thong_tin(self, attr_name):
        pass
        # return getattr(self, f"_{self.__class__.__name__}__{attr_name}", None) 
        #return getattr(self, f"_{self.__class__.__name__}__{attr_name}", None)
    def chinh_thong_tin(self, attr_name, value):
        pass
        #setattr(self, f"_{self.__class__.__name__}__{attr_name}", value)