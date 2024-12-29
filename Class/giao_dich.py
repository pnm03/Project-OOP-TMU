
class GiaoDich:
    def __init__(self, ma_giao_dich, ma_khach_hang, so_tien_thanh_toan, hanh_khach_di_cung, ngay_giao_dich, 
                 hinh_thuc_thanh_toan, trang_thai_thanh_toan, ten_chuyen_di, gia_chuyen_di, giam_gia, do_dai_chuyen_di, 
                 dia_diem_tham_quan, ngay_khoi_hanh, so_luong_hanh_khach, thoi_luong_chuyen_di, gia_phong, 
                 ten_noi_o, mo_ta, danh_gia, ten_dia_diem, ten_phuong_tien, so_luong_cho_ngoi, don_vi_cung_cap):
        """
        Khởi tạo đối tượng GiaoDich từ các tham số.
        """
        self.str_maGiaoDich = str(ma_giao_dich)
        self.str_maKhachHang = str(ma_khach_hang)
        self.str_soTienThanhToan = str(so_tien_thanh_toan)
        self.arr_hanhKhachDiCung = hanh_khach_di_cung  
        self.date_ngayGiaoDich = ngay_giao_dich
        self.str_hinhThucThanhToan = str(hinh_thuc_thanh_toan)
        self.bool_trangThaiThanhToan = trang_thai_thanh_toan == 'True'
        self.str_tenChuyenDi = ten_chuyen_di
        self.str_giaChuyenDi = str(gia_chuyen_di)
        self.str_giamGia = str(giam_gia)
        self.int_doDaiChuyenDi = int(do_dai_chuyen_di)
        self.arr_diaDiemThamQuan = dia_diem_tham_quan  
        self.date_ngayKhoiHanh = ngay_khoi_hanh
        self.int_soLuongHanhKhach = int(so_luong_hanh_khach)
        self.str_thoiLuongChuyenDi = thoi_luong_chuyen_di
        self.str_giaPhong = str(gia_phong)
        self.str_tenNoiO = ten_noi_o
        self.str_moTa = mo_ta
        self.str_danhGia = danh_gia
        self.str_tenDiaDiem = ten_dia_diem
        self.str_tenPhuongTien = ten_phuong_tien
        self.str_soLuongChoNgoi = str(so_luong_cho_ngoi)
        self.str_donViCungCap = don_vi_cung_cap

    def __str__(self):
        return (f"GiaoDich[MaGD={self.str_maGiaoDich}, MaKH={self.str_maKhachHang}, SoTienTT={self.str_soTienThanhToan}, "
                f"TenChuyenDi={self.str_tenChuyenDi}, NgayGiaoDich={self.date_ngayGiaoDich}, "
                f"TrangThaiThanhToan={self.bool_trangThaiThanhToan}]")
    
