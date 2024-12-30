from Config.setup import *
from Config.function import *
from Class.chuon_trinh_quan_ly import *

### Các thư viện dùng chung
# clear_screen() - Dọn màn hình consle
# INT_random_number(a, b) - Tra về số nguyên random từ a đến b
# pause(n) - Dừng chương trình n giây
# loading_spinner(n) - Tạo loading = progess n giây
# loading_spinner1(n) - Tạo loading = hình quay tròn n giây
# in_thong_tin(text, text_title) - text là nội dung, text_tile là tiêu đềđề
# STR_nhap_trong_khung(title, note) - title là tiêu đề, note là ghi chú; trả về string
# -> Phải có biến để hứng kết quả là string

# Tại đây khi chương trình được chạy thì đã có tất cả thư viện và màn hình được dọn sạch

# in_thong_tin("Menu", "1. Chuc nang a\n2. Chuc nang b\n3. Chuc nang c");

# Hàm chính
def main():
     try:
          quan_ly = QuanLyKhachHang()
          # print(quan_ly.khach_hang_list[0])
          # quan_ly.tao_moi_tai_khoan('a.csv')
          # quan_ly.ChucNang_them_khach_hang()
          quan_ly.ChucNang_menu()
     except KeyboardInterrupt:
          in_thong_tin_loi("Lỗi", f"Chương trình gặp lỗi không mong muốn. Đóng chương trình")
     except Exception as e:
          in_thong_tin_loi("Lỗi", f"Chương trình gặp lỗi không mong muốn. Đóng chương trình")
     finally:
          print()
          in_thong_tin("", "Đóng chương trình. Cảm ơn bạn đã sử dụng")

# Chạy chương trình
if __name__ == "__main__":
    main()