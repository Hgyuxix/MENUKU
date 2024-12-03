import qrcode

# Fungsi untuk menampilkan menu
def show_menu():
    print("=== Menu Caffeshop ===")
    for item, price in menu.items():
        print(f"{item}: Rp{price}")

# Fungsi untuk menambahkan item ke pesanan
def add_to_order(order, item, quantity):
    if item in menu:
        order[item] = order.get(item, 0) + quantity
        print(f"✅ {quantity}x {item} ditambahkan ke pesanan Anda.")
    else:
        print(f"⚠ {item} tidak ada di menu.")

# Fungsi untuk melihat pesanan
def view_order(order):
    if not order:
        print("Pesanan Anda kosong.")
    else:
        print("=== Pesanan Anda ===")
        total = 0
        for item, quantity in order.items():
            price = menu[item] * quantity
            total += price
            print(f"{item} ({quantity}x): Rp{price}")
        print(f"Total: Rp{total}")
        
from PIL import Image

# Fungsi untuk menampilkan menu
def show_menu():
    print("=== Menu Caffeshop ===")
    for item, price in menu.items():
        print(f"{item}: Rp{price}")

# Fungsi untuk menambahkan item ke pesanan
def add_to_order(order, item, quantity):
    if item in menu:
        order[item] = order.get(item, 0) + quantity
        print(f"✅ {quantity}x {item} ditambahkan ke pesanan Anda.")
    else:
        print(f"⚠ {item} tidak ada di menu.")

# Fungsi untuk melihat pesanan
def view_order(order):
    if not order:
        print("Pesanan Anda kosong.")
    else:
        print("=== Pesanan Anda ===")
        total = 0
        for item, quantity in order.items():
            price = menu[item] * quantity
            total += price
            print(f"{item} ({quantity}x): Rp{price}")
        print(f"Total: Rp{total}")

# Fungsi untuk menampilkan QR Code yang sudah ada
def show_existing_qr_code():
    try:
        # Memuat QR Code dari file (misalnya 'my_qr_code.png')
        qr_code_img = Image.open('my_qr_code.png')
        qr_code_img.show()  # Menampilkan gambar menggunakan aplikasi default
        print("✅ QR Code ditampilkan.")
    except FileNotFoundError:
        print("⚠ File QR Code tidak ditemukan.")

# Menu caffeshop
menu = {
    "Espresso": 20000,
    "Latte": 25000,
    "Cappuccino": 30000,
    "Mocha": 35000,
    "Tea": 15000,
    "Cake Slice": 20000
}

# Pesanan pelanggan
order = {}

# Antarmuka sistem
while True:
    print("\n=== Caffeshop ===")
    print("1. Lihat Menu")
    print("2. Tambah ke Pesanan")
    print("3. Lihat Pesanan")
    print("4. Tampilkan QR Code Saya")
    print("5. Keluar")
    
    choice = input("Pilih opsi (1-5): ")
    
    if choice == "1":
        show_menu()
    elif choice == "2":
        item = input("Masukkan nama item: ")
        try:
            quantity = int(input("Masukkan jumlah: "))
            add_to_order(order, item, quantity)
        except ValueError:
            print("⚠ Jumlah harus berupa angka.")
    elif choice == "3":
        view_order(order)
    elif choice == "4":
        show_existing_qr_code()  # Menampilkan QR Code Anda sendiri
    elif choice == "5":
        print("Terima kasih telah mengunjungi caffeshop kami!")
        break
    else:
        print("⚠ Pilihan tidak valid, silakan coba lagi.")