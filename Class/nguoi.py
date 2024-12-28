class Nguoi:
     def __init__(self, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email):
        """
        Khởi tạo đối tượng Nguoi từ các tham số.
        """
        self.str_hoTen = ho_ten
        self.date_ngaySinh = ngay_sinh  
        self.str_diaChi = dia_chi
        self.int_soDienThoai = so_dien_thoai
        self.str_email = email

     def __str__(self):
        return (f"Nguoi[HoTen={self.str_hoTen}, NgaySinh={self.date_ngaySinh}, "
                f"DiaChi={self.str_diaChi}, SoDienThoai={self.int_soDienThoai}, Email={self.str_email}]")
     def get_email (self):
         return self.str_email
     def get_sdt (self):
         return self.int_soDienThoai