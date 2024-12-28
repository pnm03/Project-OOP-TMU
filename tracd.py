class QuanLyKhachHang:
    ...

    def them_khach_hang_thu_cong(self):
        try:
            print("--- THÊM KHÁCH HÀNG THỦ CÔNG ---")
            str_hoTen = 
            input("Nhập họ tên: ")
            date_ngaySinh = input("Nhập ngày sinh (YYYY-MM-DD): ")
            str_diaChi = input("Nhập địa chỉ: ")
            int_soDienThoai = input("Nhập số điện thoại: ")
            str_email = input("Nhập email: ")

            # Kiểm tra nếu khách hàng đã tồn tại trong database
            if self.kiem_tra_khach_hang_ton_tai(str_email, int_soDienThoai):
                print(f"Khách hàng với email {str_email} hoặc số điện thoại {int_soDienThoai} đã tồn tại.")
                return

            # Tạo mã khách hàng mới và mật khẩu
            ma_khach_hang = self.STR_tao_moi_makhachhang()
            mat_khau = self.STR_tao_mat_khau()

            # Hiển thị thông tin để xác nhận
            print("\n--- XÁC NHẬN THÔNG TIN KHÁCH HÀNG ---")
            print(f"Họ tên: {str_hoTen}")
            print(f"Ngày sinh: {date_ngaySinh}")
            print(f"Địa chỉ: {str_diaChi}")
            print(f"Số điện thoại: {int_soDienThoai}")
            print(f"Email: {str_email}")
            print(f"Mã khách hàng: {ma_khach_hang}")
            print(f"Mật khẩu tài khoản: {mat_khau}")

            xac_nhan = input("\nXác nhận lưu khách hàng này? (y/n): ")
            if xac_nhan.lower() != 'y':
                print("Hủy thao tác thêm khách hàng.")
                return

            # Lưu khách hàng và tài khoản vào danh sách
            khach_hang = KhachHang(
                str_hoTen, date_ngaySinh, str_diaChi, int_soDienThoai, str_email,
                ma_khach_hang, False, "0", 0, datetime.today().strftime('%Y-%m-%d'), 0, "0"
            )
            self.khach_hang_list.append(khach_hang)

            tai_khoan = TaiKhoan(
                str_email, mat_khau, ma_khach_hang, True, 0
            )
            self.tai_khoan_list.append(tai_khoan)

            print("Thêm khách hàng thành công!")
            self.luu_du_lieu_vao_file()

        except Exception as e:
            print(f"Đã xảy ra lỗi khi thêm khách hàng bằng tay: {e}")

    def tao_moi_tai_khoan(self, file_path):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Bỏ qua dòng tiêu đề

                khach_hang_moi = []
                for row in reader:
                    str_hoTen, date_ngaySinh, str_diaChi, int_soDienThoai, str_email, *_ = row

                    if self.kiem_tra_khach_hang_ton_tai(str_email, int_soDienThoai):
                        print(f"Bỏ qua: Khách hàng với email {str_email} hoặc số điện thoại {int_soDienThoai} đã tồn tại.")
                        continue

                    ma_khach_hang = self.STR_tao_moi_makhachhang()
                    mat_khau = self.STR_tao_mat_khau()

                    khach_hang_moi.append((
                        KhachHang(
                            str_hoTen, date_ngaySinh, str_diaChi, int_soDienThoai, str_email,
                            ma_khach_hang, False, "0", 0, datetime.today().strftime('%Y-%m-%d'), 0, "0"
                        ),
                        TaiKhoan(
                            str_email, mat_khau, ma_khach_hang, True, 0
                        )
                    ))

                # Hiển thị thông tin khách hàng mới
                print("\n--- XÁC NHẬN DANH SÁCH KHÁCH HÀNG MỚI ---")
                for idx, (kh, tk) in enumerate(khach_hang_moi, start=1):
                    print(f"Khách hàng {idx}: Họ tên: {kh.str_hoTen}, Ngày sinh: {kh.date_ngaySinh}, Địa chỉ: {kh.str_diaChi}, Số điện thoại: {kh.int_soDienThoai}, Email: {kh.str_email}, Mã KH: {kh.str_maKhachHang}, Mật khẩu: {tk.str_matKhau}")

                xac_nhan = input("\nXác nhận lưu toàn bộ khách hàng này? (y/n): ")
                if xac_nhan.lower() != 'y':
                    print("Hủy thao tác thêm từ file.")
                    return

                # Lưu khách hàng vào danh sách
                for kh, tk in khach_hang_moi:
                    self.khach_hang_list.append(kh)
                    self.tai_khoan_list.append(tk)

                print("Thêm khách hàng từ file thành công!")
                self.luu_du_lieu_vao_file()

        except Exception as e:
            print(f"Đã xảy ra lỗi khi thêm khách hàng từ file: {e}")
