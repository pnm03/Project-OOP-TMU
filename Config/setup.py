import subprocess
import sys
import signal
import sys
import time
from Config.function import *

# Đọc các thư viện từ file cấu hình
from Config.library import libraries

# Hàm xử lý khi người dùng nhấn phím tạo ra lỗi dừng đột ngột
def handle_interrupt(signal, frame):
     sys.exit(1)  # Thoát chương trình

# Đăng ký xử lý tín hiệu SIGINT
signal.signal(signal.SIGINT, handle_interrupt)

# Cài đặt thư viện
def install_libraries(libraries):
     for library in libraries:
          try:
               __import__(library)
               print(f"{library} đã được tải thành công.")
          except ImportError:
               print(f"{library} Thư viện này chưa được cài đặt. Vui lòng xem thêm tại Gfi/LIBRARY")
               user_input = input(f"Bạn có muốn cài đặt {library} không? (y/n): ")
               if user_input.lower() == 'y':
                    print(f"Đang cài đặt {library}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", library])
                    #print(f"{library} đã được cài đặt.")
                    clear_screen()
               else:
                    print(f"Không cài đặt {library}. Dừng chương trình")
                    sys.exit()

# Cài đặt các thư viện từ config
install_libraries(libraries)
print("Tải thông tin hoàn tất!")
loading_spinner1(1)
clear_screen()