import time
import os
import sys
import random
from datetime import datetime
import re
# Import tất cả thư viện tại đây
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Tạo hàm dùng chung thì comment tại main để người khác dùng với

def STR_chuan_hoa_text(text):
    #Chuẩn hóa tên: chữ cái đầu viết hoa, giữa các từ chỉ có 1 dấu cách.
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    # Xóa các khoảng trắng thừa và ký tự không cần thiết ở đầu và cuối
    text = text.strip()

    # Thay thế nhiều khoảng trắng liên tiếp thành 1 khoảng trắng
    text = re.sub(r'\s+', ' ', text)

    # Viết hoa chữ cái đầu của mỗi từ
    text = text.title()

    return text

# Kiểm tra định dạng số điện thoại
def BOOL_kiem_tra_so_dien_thoai(so_dien_thoai):
    pattern = r"^0\d{9,11}$"
    return bool(re.match(pattern, so_dien_thoai))
# Kiểm tra định dạng email 
def BOOL_kiem_tra_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))
# Kiểm tra định dạng ngày
def BOOL_kiem_tra_ngay_sinh(ngay_sinh):
    try:
        datetime.strptime(ngay_sinh, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Hàm tạo độ ngưng
def tiep_tuc():
    input("Ấn phím bất kỳ để tiếp tục...")

# Hàm nhập thông tin theo khung
def STR_nhap_trong_khung(
     text_title="",
     subtitle="", 
     style_title="bold cyan", 
     border_style="cyan",  
     width=None
):
    """
    Hiển thị khung để người dùng nhập thông tin trong khuôn.

    Args:
        text_title (str): Tiêu đề của khung.
        style_title (str): Kiểu định dạng tiêu đề.
        border_style (str): Màu sắc viền khung.
        subtitle (str): Phụ đề bên dưới khung.
        width (int): Độ rộng của khung.
    
    Returns:
        str: Thông tin do người dùng nhập.
    """
    console = Console()

    console.print(
        Panel(
            "Nhập thông tin...", 
            title=text_title, 
            title_align="left",
            border_style=border_style, 
            subtitle=subtitle + ", ấn enter để tiếp tục",
            #expand=False, 
            width=60
        )
    )

    # Bước 2: Nhận thông tin`` từ người dùng
    #user_input = input("> ")
    prompt = "\033[5m\033[31m\033[1m> \033[0m"
    user_input = input(prompt)

    return user_input

# Hàm in thông tin theo khung
def in_thong_tin(
    text_title="", 
    text="", 
    style_title="bold cyan", 
    border_style="bold cyan", 
    subtitle=None, 
    expand=False, 
    width=None):
    """
    Hiển thị thông tin trong khung.
        text (str): Nội dung hiển thị bên trong khung.
        text_title (str): Tiêu đề của khung (mặc định là "None").
        style_title (str): Kiểu định dạng tiêu đề (mặc định là "bold white").
        border_style (str): Màu sắc viền (mặc định là "blue").
        subtitle (str): Phụ đề xuất hiện dưới khung (mặc định là None).
        expand (bool): Nếu True, khung sẽ giãn theo chiều rộng màn hình (mặc định là False).
        width (int): Độ rộng của khung. Nếu None, sẽ tự động tính theo nội dung (mặc định là None).
    """
    console = Console()
    
    # Tạo tiêu đề với kiểu định dạng
    title_text = Text(text_title, style=style_title)
    
    # Tạo khung hiển thị
    console.print(
        Panel(
            text, 
            title=text_title, 
            border_style=border_style, 
            #title_align="left",
            expand=expand, 
            subtitle=subtitle, 
            width=width
        )
    )
# Hàm in thông tin lỗi theo khung
def in_thong_tin_loi (
    text_title="", 
    text="", 
    style_title="red", 
    border_style="red", 
    subtitle=None, 
    expand=False, 
    width=None):
    """
    Hiển thị thông tin trong khung.
        text (str): Nội dung hiển thị bên trong khung.
        text_title (str): Tiêu đề của khung (mặc định là "None").
        style_title (str): Kiểu định dạng tiêu đề (mặc định là "bold white").
        border_style (str): Màu sắc viền (mặc định là "blue").
        subtitle (str): Phụ đề xuất hiện dưới khung (mặc định là None).
        expand (bool): Nếu True, khung sẽ giãn theo chiều rộng màn hình (mặc định là False).
        width (int): Độ rộng của khung. Nếu None, sẽ tự động tính theo nội dung (mặc định là None).
    """
    console = Console()
    
    # Tạo tiêu đề với kiểu định dạng
    title_text = Text(text_title, style=style_title)
    
    # Tạo khung hiển thị
    console.print(
        Panel(
            text, 
            title=text_title, 
            border_style=border_style, 
            title_align="left",
            expand=expand, 
            subtitle=subtitle, 
            width=width
        )
    )

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
            result = INT_random_number(8, 10)
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