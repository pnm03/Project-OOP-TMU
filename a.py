import csv
import random
from datetime import datetime, timedelta
from faker import Faker
from faker.providers import automotive

# Khởi tạo Faker
fake = Faker()

# Kiểm tra xem provider automotive có sẵn không
try:
    fake.add_provider(automotive)
    vehicle_makes = [fake.vehicle_make() for _ in range(10)]  # Nếu automotive provider có sẵn
except AttributeError:
    # Nếu không có, sử dụng danh sách các hãng xe giả định
    vehicle_makes = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Mercedes", "Audi", "Hyundai", "Nissan", "Tesla"]

def generate_date_in_range(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

def generate_fake_data(customer_id):
    return {
        # Người
        "str_maKhachHang": customer_id,  # Mã khách hàng giống nhau
        "str_hoTen": fake.name(),
        "date_ngaySinh": generate_date_in_range(1970, 2000),
        "str_diaChi": fake.address(),
        "int_soDienThoai": fake.msisdn(),
        "str_email": fake.email(),
        # Khách hàng
        "str_maKhachHang": customer_id,
        "bool_hangKhachHang": random.choice([True, False]),
        "str_soTienDaGiaoDich": f"{random.randint(100, 10000)} USD",
        "int_soLuongGiaoDich": random.randint(1, 100),
        "date_ngayTaoTaiKhoan": generate_date_in_range(2010, 2023),
        "int_diemTichLuy": random.randint(0, 5000),
        "str_soTienTietKiem": f"{random.randint(1000, 50000)} USD",
        # Giao dịch
        "str_maKhachHang": customer_id,
        "str_maGiaoDich": fake.uuid4(),
        "str_soTienThanhToan": f"{random.randint(100, 5000)} USD",
        "arr_hanhKhachDiCung": {f"Passenger_{i}": fake.name() for i in range(1, random.randint(1, 5))},
        "date_ngayGiaoDich": generate_date_in_range(2015, 2024),
        "bool_hinhThucThanhToan": random.choice(["Card", "Cash"]),
        "bool_trangThaiThanhToan": random.choice([True, False]),
        "str_tenChuyenDi": fake.city(),
        "string_giaChuyenDi": f"{random.randint(500, 2000)} USD",
        "str_giamGia": f"{random.randint(0, 50)}%",
        "int_doDaiChuyenDi": random.randint(1, 14),
        "arr_diaDiemThamQuan": {fake.city(): fake.address() for _ in range(random.randint(1, 3))},
        "date_ngayKhoiHanh": generate_date_in_range(2023, 2024),
        "int_soLuongHanhKhach": random.randint(1, 50),
        "str_thoiLuongChuyenDi": f"{random.randint(1, 24)} hours",
        "str_giaPhong": f"{random.randint(50, 500)} USD",
        "str_tenNoiO": fake.company(),
        "str_moTa": fake.text(max_nb_chars=200),
        "str_danhGia": f"{random.randint(1, 5)} stars",
        "str_tenDiaDiem": fake.city(),
        "str_tenPhuongTien": random.choice(vehicle_makes),  # Sử dụng danh sách hãng xe
        "str_soLuongChoNgoi": f"{random.randint(2, 8)}",
        "str_donViCungCap": fake.company()
    }

# Ghi dữ liệu vào tệp CSV
try:
    # Tạo một mã khách hàng duy nhất
    customer_id = fake.uuid4()

    # Lấy danh sách các trường dữ liệu
    fieldnames = generate_fake_data(customer_id).keys()

    with open("a.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Tạo 10 hàng dữ liệu giả
        for _ in range(10):
            writer.writerow(generate_fake_data(customer_id))

    print("Tệp 'a.csv' đã được tạo thành công.")

except Exception as e:
    print("Đã xảy ra lỗi:", e)
