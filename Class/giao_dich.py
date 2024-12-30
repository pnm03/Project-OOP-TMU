class GiaoDich:
    def __init__(self, ma_giao_dich, ma_khach_hang, so_tien_thanh_toan, hanh_khach_di_cung, ngay_giao_dich, 
                 hinh_thuc_thanh_toan, trang_thai_thanh_toan, ten_chuyen_di, gia_chuyen_di, giam_gia, do_dai_chuyen_di, 
                 dia_diem_tham_quan, ngay_khoi_hanh, so_luong_hanh_khach, thoi_luong_chuyen_di, gia_phong, 
                 ten_noi_o, mo_ta, danh_gia, ten_dia_diem, ten_phuong_tien, so_luong_cho_ngoi, don_vi_cung_cap):
        """
        Khởi tạo đối tượng GiaoDich từ các tham số.
        """
        self.__str_maGiaoDich = str(ma_giao_dich)
        self.__str_maKhachHang = str(ma_khach_hang)
        self.__str_soTienThanhToan = str(so_tien_thanh_toan)
        self.__arr_hanhKhachDiCung = hanh_khach_di_cung  
        self.__date_ngayGiaoDich = ngay_giao_dich
        self.__str_hinhThucThanhToan = str(hinh_thuc_thanh_toan)
        self.__bool_trangThaiThanhToan = trang_thai_thanh_toan == 'True'
        self.__str_tenChuyenDi = ten_chuyen_di
        self.__str_giaChuyenDi = str(gia_chuyen_di)
        self.__str_giamGia = str(giam_gia)
        self.__int_doDaiChuyenDi = int(do_dai_chuyen_di)
        self.__arr_diaDiemThamQuan = dia_diem_tham_quan  
        self.__date_ngayKhoiHanh = ngay_khoi_hanh
        self.__int_soLuongHanhKhach = int(so_luong_hanh_khach)
        self.__str_thoiLuongChuyenDi = thoi_luong_chuyen_di
        self.__str_giaPhong = str(gia_phong)
        self.__str_tenNoiO = ten_noi_o
        self.__str_moTa = mo_ta
        self.__str_danhGia = danh_gia
        self.__str_tenDiaDiem = ten_dia_diem
        self.__str_tenPhuongTien = ten_phuong_tien
        self.__str_soLuongChoNgoi = str(so_luong_cho_ngoi)
        self.__str_donViCungCap = don_vi_cung_cap

    def __str__(self):
        return (f"GiaoDich[MaGD={self.__str_maGiaoDich}, MaKH={self.__str_maKhachHang}, SoTienTT={self.__str_soTienThanhToan}, "
                f"TenChuyenDi={self.__str_tenChuyenDi}, NgayGiaoDich={self.__date_ngayGiaoDich}, "
                f"TrangThaiThanhToan={self.__bool_trangThaiThanhToan}]")
    
    def hien_thi_thong_tin(self):
        print(self)
        
    def hien_thi_thong_tin_giao_dich(self):
        print(f"\nChi Tiết Giao Dịch:\n")
        print(f"Mã Giao Dịch: {self.__str_maGiaoDich}\n")
        print(f"Mã Khách Hàng: {self.__str_maKhachHang}\n")
        print(f"Số Tiền Thanh Toán: {self.__str_soTienThanhToan}\n")
        print(f"Hành Khách Đi Cùng: {', '.join(self.__arr_hanhKhachDiCung)}\n")
        print(f"Ngày Giao Dịch: {self.__date_ngayGiaoDich}\n")
        print(f"Hình Thức Thanh Toán: {self.__str_hinhThucThanhToan}\n")
        print(f"Trạng Thái Thanh Toán: {'Đã Thanh Toán' if self.__bool_trangThaiThanhToan else 'Chưa Thanh Toán'}\n")
        print(f"Tên Chuyến Đi: {self.__str_tenChuyenDi}\n")
        print(f"Giá Chuyến Đi: {self.__str_giaChuyenDi}\n")
        print(f"Giảm Giá: {self.__str_giamGia}\n")
        print(f"Độ Dài Chuyến Đi: {self.__int_doDaiChuyenDi} km\n")
        print(f"Địa Điểm Tham Quan: {', '.join(self.__arr_diaDiemThamQuan)}\n")
        print(f"Ngày Khởi Hành: {self.__date_ngayKhoiHanh}\n")
        print(f"Số Lượng Hành Khách: {self.__int_soLuongHanhKhach}\n")
        print(f"Thời Lượng Chuyến Đi: {self.__str_thoiLuongChuyenDi}\n")
        print(f"Giá Phòng: {self.__str_giaPhong}\n")
        print(f"Tên Nơi Ở: {self.__str_tenNoiO}\n")
        print(f"Mô Tả: {self.__str_moTa}\n")
        print(f"Đánh Giá: {self.__str_danhGia}\n")
        print(f"Tên Địa Điểm: {self.__str_tenDiaDiem}\n")
        print(f"Tên Phương Tiện: {self.__str_tenPhuongTien}\n")
        print(f"Số Lượng Chỗ Ngồi: {self.__str_soLuongChoNgoi}\n")
        print(f"Đơn Vị Cung Cấp: {self.__str_donViCungCap}\n")


    def lay_thong_tin(self, attr_name):
        """Lấy thông tin của giao dịch dựa trên tên thuộc tính."""
        return getattr(self, f"_{self.__class__.__name__}__{attr_name}", None)
