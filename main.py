from Config.setup import *
from Config.function import *
from Class.chuon_trinh_quan_ly import *

def main():
     try:
          quan_ly = QuanLyKhachHang()
          quan_ly.kiem_tra_dang_nhap()
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