from Config.setup import *
from Config.function import *
from Class.chuon_trinh_quan_ly import *

### Các thư viện dùng chung
# INT_random_number(a, b) - Tra về số nguyên random từ a đến b
# pause(n) - Dừng chương trình n giây
# loading_spinner(n) - Tạo loading = progess n giây
# loading_spinner1(n) - Tạo loading = hình quay tròn n giây
# in_thong_tin(text, text_title) - text là nội dung, text_tile là tiêu đềđề
# STR_nhap_trong_khung(title, note) - title là tiêu đề, note là ghi chú; trả về string
# -> Phải có biến để hứng kết quả là string

# Tại đây khi chương trình được chạy thì đã có tất cả thư viện và màn hình được dọn sạch
STR_nhap_trong_khung("Nhập họ tên", "Nhập số")

in_thong_tin("Menu", "1. Chuc nang a\n2. Chuc nang b\n3. Chuc nang c");

quan_ly = QuanLyKhachHang()
quan_ly1 = QuanLyKhachHang()
quan_ly.doc_du_lieu_tu_file()