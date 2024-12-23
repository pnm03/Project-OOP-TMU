import time
import os
import sys
import random
# Import tất cả thư viện tại đây
from rich.progress import Progress

# Tạo hàm dùng chung thì comment tại main để người khác dùng với

# Hàm trả về số ngẫu nhiên trong khoảng từ a đến b
def INT_random_number(a, b):
    return random.randint(a, b) 

# Tạm dừng chương trình trong thời gian cho trước
def pause(seconds):
    time.sleep(seconds)

# Hiệu ứng loading progess bar :3
def loading_spinner(duration):
    with Progress() as progress:
        task = progress.add_task("[cyan]Loading...", total=100)
        
        # Lưu thời gian bắt đầu
        start_time = time.time()  # Đặt thời gian bắt đầu tại đây
        
        while not progress.finished:
            time.sleep(0.1)
            result = INT_random_number(5, 8)
            progress.update(task, advance=result) # Tăng random mỗi lần :v
            
            # Kiểm tra thời gian và dừng khi đã đủ duration
            if time.time() - start_time >= duration:
                break

# Còn đây là hiệu ứng loading quay tròn         
def loading_spinner1(duration):
    spinner = ['◜', '◝', '◞', '◟']  # Các ký tự tạo hình tròn quay
    end_time = time.time() + duration

    while time.time() < end_time:
        for char in spinner:
            sys.stdout.write(f'\r{char} Loading...')
            sys.stdout.flush()  # Đảm bảo kết quả được in ra ngay lập tức
            time.sleep(0.2) 

# Dọn màn hình
def clear_screen():
     if sys.platform == "win32":
          os.system('cls') 
     else:
          os.system('clear')

print("Đang bắt đầu chương trình...")
loading_spinner(1)